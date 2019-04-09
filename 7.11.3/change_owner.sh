#!/bin/sh

cd ${WWW_FOLDER}
chown -R ${WWW_USER}:${WWW_GROUP} .
chmod -R 755 .
chmod -R 775 cache custom modules themes data upload
chmod 775 config_override.php 2>/dev/null
