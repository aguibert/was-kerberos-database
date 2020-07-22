-- Ignore pluggable databases
alter session set "_ORACLE_SCRIPT"=true;

-- Create oracle user
CREATE USER "oracle@EXAMPLE.COM" IDENTIFIED EXTERNALLY;
GRANT CONNECT TO "oracle@EXAMPLE.COM";
GRANT CREATE SESSION TO "oracle@EXAMPLE.COM";
