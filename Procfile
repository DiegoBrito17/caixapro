web: bash -c "python migrate_sqlite_to_postgres.py && gunicorn app:app --bind 0.0.0.0:${PORT:-8080}"
