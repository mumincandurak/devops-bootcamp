#!/bin/bash
TARGET_FILE="/home/mumincan/devops-bootcamp/linux-command"
BACKUP_INDEX="./backup"
DATE=$(date +%Y-%m-%d_%H-%M)
BACKUP_NAME="backup-${DATE}.tar.gz"

if [ ! -d "$TARGET_FILE" ]; then
	echo "Error: '$TARGET_FILE' is not found!"
	exit 1
fi

echo "Backup is starting!"
echo "Source: $TARGET_FILE"
echo "TARGET: $BACKUP_INDEX/$BACKUP_NAME"

tar -czf "$BACKUP_INDEX/$BACKUP_NAME" "$TARGET_FILE" 2>/dev/null

if [ $? -eq 0 ]; then
	echo "✅ Backup completed successfully!"
else 
	echo "❌ An error occurred during the backup!"
fi
