* Stream Debuggger：`Internal Error`
  * Run > Profile > Edit Configurations > `-XX:+UseG1GC -Xms16G` 改成 `-XX:+UseG1GC -Xms2G`
* JDK isn't specified for module 'XXX'
  * File > Settings > Build, Execution, Deployment > Build Tools > Maven > Maven home path：選 Bundled (Maven 3)
  * Run > Profile > Edit Configurations > make sure jave version and working directory is right
