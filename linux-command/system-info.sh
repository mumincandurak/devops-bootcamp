#!/bin/bash
echo "DATE: $(date)"
echo "I am $(whoami)."
echo "DISK USAGE:"
echo "$(df -h)"
echo "Empty RAM:"
echo "$(free -h)"
