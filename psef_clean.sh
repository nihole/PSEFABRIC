rm $PSEFABRIC/PSEF_CONF/*
rm $PSEFABRIC/PSEF_CONF/EQ_CONF/*
rm $PSEFABRIC/PSEF_LOGS/*
cd $CONFD_DIR/myprojects/psefabric/
make stop clean
