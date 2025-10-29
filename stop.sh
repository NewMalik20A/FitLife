#!/bin/bash

# FitLife Blog - Stop Script

echo "🛑 Stopping FitLife Blog..."
echo ""

docker-compose down

echo ""
echo "✅ All services stopped"
echo ""
echo "To start again, run: ./start.sh"
echo "To remove all data, run: docker-compose down -v"
