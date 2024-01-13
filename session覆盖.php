<?php
ini_set('session.serialize_handler', 'php_binary');
session_save_path("D:\\phpstudy_pro\\WWW\\WWW\\");
session_start();

$_SESSION['username'] = 'admin';
