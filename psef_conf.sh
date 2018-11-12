export PROJECT=/opt/QA/PSEFABRIC/PROJECTS/p000
export PSEFABRIC=/opt/QA/PSEFABRIC
export CONFD_DIR=/opt/QA/CONFD
cp $PROJECT/PSEF_YANG/* $CONFD_DIR/myprojects/psefabric/
cd $CONFD_DIR/myprojects/psefabric/
/opt/QA/CONFD/bin/confdc -c psefabric-types.yang
/opt/QA/CONFD/bin/confdc -c structure.yang
/opt/QA/CONFD/bin/confdc -c policy.yang
