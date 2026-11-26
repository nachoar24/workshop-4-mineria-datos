"""Exporta datos reales de Oracle; no usa archivos Northwind."""
import csv
import getpass
import hashlib
import json
import os
from pathlib import Path
from datetime import datetime, timezone
import oracledb

root = Path(__file__).resolve().parent
out = root / "datos" / "invacom_dw"
out.mkdir(parents=True, exist_ok=True)
sql = (root / "sql/01_extraccion_invacom_dw.sql").read_text(encoding="utf-8").strip().rstrip(";")
dsn = os.environ.get("ORACLE_DSN") or input("DSN Oracle (host:1521/servicio): ")
user = os.environ.get("ORACLE_USER", "INVACOM_DW")
password = os.environ.get("ORACLE_PASSWORD") or getpass.getpass("Contraseña Oracle: ")
with oracledb.connect(user=user, password=password, dsn=dsn) as conn:
    with conn.cursor() as cur:
        cur.execute(sql)
        columns = [c[0] for c in cur.description]
        rows = cur.fetchall()
        cur.execute("SELECT COUNT(*), SUM(CANTIDAD_VENDIDA), SUM(IMPORTE_BRUTO), SUM(IMPORTE_DESCUENTO), SUM(IMPORTE_NETO) FROM INVACOM_DW.FACT_VENTAS")
        totals = cur.fetchone()
assert rows and len(rows) == totals[0], "Extracción incompleta"
assert len({(r[1], r[2]) for r in rows}) == len(rows), "Claves duplicadas"
from decimal import Decimal
for idx, expected in zip(range(12,16), totals[1:]):
    assert sum(Decimal(str(r[idx])) for r in rows) == Decimal(str(expected)), columns[idx]
path = out / "invacom_dw_ventas.csv"
with path.open("w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(columns)
    writer.writerows(rows)
manifest = {"source": "Oracle INVACOM_DW", "extracted_at_utc": datetime.now(timezone.utc).isoformat(), "rows": len(rows), "sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "totals": dict(zip(["lineas","unidades","bruto","descuento","neto"], map(str,totals)))}
(out / "manifest.json").write_text(json.dumps(manifest, indent=2)+"\n", encoding="utf-8")
print(json.dumps(manifest, indent=2))
