AdminApp.install('/work/app/was-kerberos-database.war', '[ -nopreCompileJSPs -distributeApp -nouseMetaDataFromBinary -appname was-kerberos-database_war -createMBeansForResources -noreloadEnabled -nodeployws -validateinstall warn -noprocessEmbeddedConfig -filepermission .*\.dll=755#.*\.so=755#.*\.a=755#.*\.sl=755 -noallowDispatchRemoteInclude -noallowServiceRemoteInclude -asyncRequestDispatchType DISABLED -nouseAutoLink -noenableClientModule -clientMode isolated -novalidateSchema -contextroot /was-kerberos-database -MapResRefToEJB [[ was-kerberos-database.war "" was-kerberos-database.war,WEB-INF/web.xml jdbc/db2ds javax.sql.DataSource jdbc/db2ds "" "" "" ]] -MapModulesToServers [[ was-kerberos-database.war was-kerberos-database.war,WEB-INF/web.xml WebSphere:cell=DefaultCell01,node=DefaultNode01,server=server1 ]] -MapWebModToVH [[ was-kerberos-database.war was-kerberos-database.war,WEB-INF/web.xml default_host ]] -CtxRootForWebMod [[ was-kerberos-database.war was-kerberos-database.war,WEB-INF/web.xml /was-kerberos-database ]]]' ) 
AdminConfig.save()