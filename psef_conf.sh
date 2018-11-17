bash -c "more ./env > /etc/profile.d/psef_conf.sh"
sh /etc/profile.d/psef_conf.sh
cp $PROJECT/PSEF_YANG/* $CONFD_DIR/myprojects/psefabric/
cd $CONFD_DIR/myprojects/psefabric/
/opt/QA/CONFD/bin/confdc -c psefabric-types.yang
/opt/QA/CONFD/bin/confdc -c structure.yang
/opt/QA/CONFD/bin/confdc -c policy.yang
