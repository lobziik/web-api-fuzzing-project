#!/bin/bash
set -e

# Wait for Postgres
{
  while ! echo -n > /dev/tcp/db/5432;
  do
    sleep 0.1;
  done;
} 2>/dev/null

exec "$@"
