echo "export PROJECT=/opt/QA/PSEFABRIC/PROJECTS/p002" > /etc/profile.d/psef_conf.sh
echo "export PSEFABRIC=/opt/QA/PSEFABRIC" >> /etc/profile.d/psef_conf.sh
echo "export CONFD_DIR=/opt/QA/CONFD" >> /etc/profile.d/psef_conf.sh
sh /etc/profile.d/psef_conf.sh
cp $PROJECT/PSEF_YANG/* $CONFD_DIR/myprojects/psefabric/
cd $CONFD_DIR/myprojects/psefabric/
/opt/QA/CONFD/bin/confdc -c psefabric-types.yang
/opt/QA/CONFD/bin/confdc -c structure.yang
/opt/QA/CONFD/bin/confdc -c policy.yang
