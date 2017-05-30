######################################################################
# Introduction example 7-c_actions
# (C) 2006 Tail-f Systems
#
# See the README file for more information
######################################################################

usage:
	@echo "See README file for more instructions"
	@echo "make all     Build all example files"
	@echo "make clean   Remove all built and intermediary files"
	@echo "make start   Start CONFD daemon and example agent"
	@echo "make stop    Stop any CONFD daemon and example agent"
	@echo "make query   Run query against CONFD"
	@echo "make cli     Start the CONFD Command Line Interface"

######################################################################
# Where is ConfD installed? Make sure CONFD_DIR points it out
CONFD_DIR ?= ../../..

# Include standard ConfD build definitions and rules
include $(CONFD_DIR)/src/confd/build/include.mk

# In case CONFD_DIR is not set (correctly), this rule will trigger
$(CONFD_DIR)/src/confd/build/include.mk:
	@echo 'Where is ConfD installed? Set $$CONFD_DIR to point it out!'
	@echo ''

######################################################################
# Example specific definitions and rules

CONFD_FLAGS = --addloadpath $(CONFD_DIR)/etc/confd
START_FLAGS ?= 

OSTYPE	= $(shell uname -s)
SRC	= psefabric-conf.c
OBJS	= $(SRC:.c=.o)
CFLAGS	+= -D$(OSTYPE)


#all:	resolved-policy.fxs *.fxs gbp-common.fxs $(CDB_DIR) ssh-keydir
LST     = ietf-inet-types.fxs ietf-packet-fields.fxs psefabric-types.fxs policy.fxs structure.fxs
all:    $(LST) psefabric-conf  $(CDB_DIR) ssh-keydir
	@echo "Build complete"

psefabric-conf: policy.h $(OBJS)
	$(CC) -o $@ $(OBJS) $(LIBS)

######################################################################
clean:	iclean
	-rm -rf policy.h  2> /dev/null || true

start:  stop start_confd start_subscriber

start_confd:
	$(CONFD) -c confd.conf $(CONFD_FLAGS)

start_subscriber:
	./psefabric-conf $(START_FLAGS)


######################################################################
stop:
	### Killing any confd daemon and ARP confd agents
	$(CONFD) --stop || true
	$(KILLALL) psefabric-conf || true

######################################################################
cli:
	$(CONFD_DIR)/bin/confd_cli --user=admin --groups=admin \
		--interactive || echo Exit

cli-c:
	$(CONFD_DIR)/bin/confd_cli -C --user=admin --groups=admin \
		--interactive || echo Exit

cli-j:
	$(CONFD_DIR)/bin/confd_cli -J --user=admin --groups=admin \
		--interactive || echo Exit

######################################################################
query:
	$(CONFD_DIR)/bin/netconf-console-tcp cmd-invoke-action.xml

query2:
	$(CONFD_DIR)/bin/netconf-console-tcp cmd-invoke-action2.xml

query-err:
	$(CONFD_DIR)/bin/netconf-console-tcp cmd-invoke-action-err.xml

######################################################################
