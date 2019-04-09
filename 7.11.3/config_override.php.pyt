<?php
  if(null !== $$installer_defaults) {
    $$installer_defaults['setup_db_host_name']            = '$db_host_name';
    $$installer_defaults['setup_db_database_name']        = '$database_name';
    $$installer_defaults['setup_db_admin_user_name']      = '$db_user_name';
    $$installer_defaults['setup_db_admin_password']       = '$db_password';
    $$installer_defaults['db_type']                       = '$db_type';
  }

  if(null !== $$sugar_config) {
    $$sugar_config['dbconfig']['db_port'] = 3306;
    $$sugar_config['dbconfig']['db_manager'] = '$db_manager';
    $$sugar_config['dbconfig']['db_host_name'] = '$db_host_name';
    $$sugar_config['dbconfig']['db_user_name'] = '$db_user_name';
    $$sugar_config['dbconfig']['db_password'] = '$db_password';
    $$sugar_config['default_permissions']['dir_mode'] = 1533;
    $$sugar_config['default_permissions']['file_mode'] = 436;
    $$sugar_config['default_permissions']['user'] = 'www-data';
    $$sugar_config['default_permissions']['group'] = 'www-data';
  }
?>
