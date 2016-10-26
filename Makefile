.PHONY: default install
prefix = /usr/local
bindir = $(prefix)/bin
mandir = $(prefix)/share/man

default:

install:
	install -D xpaste $(bindir)/xpaste
	install -D -m644 xpaste.1x $(mandir)/man1/xpaste.1x
	gzip $(mandir)/man1/xpaste.1x
