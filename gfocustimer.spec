Summary: Prepare timesheet from X window usage
Distribution: None
Vendor: James Cameron
Name: gfocustimer
Version: 0.4
Release: 1
Copyright: GPL
Packager: quozl@us.netrek.org
URL: http://quozl.us.netrek.org/gfocustimer/
Group: Applications/Productivity
Source: gfocustimer-0.4.tar.gz
BuildRoot: /tmp/%{name}-root

%description
gfocustimer  captures  information about which windows you
are  spending  your  time  in,  to  assist  with  personal
scheduling and preparing timesheets.

gfocustimer  displays a list of chargable tasks which con-
sist of an entry name and the time spent on the task.   It
can be used in a manual mode, where the user selects a new
entry, or in a semi-automatic focus watching  mode,  where
the user connects windows on screen to tasks.

%prep
%setup

%build
pwd
./configure --prefix=/usr
make

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin/
install src/gfocustimer $RPM_BUILD_ROOT/usr/bin/
mkdir -p $RPM_BUILD_ROOT/usr/man/man1/
install gfocustimer.1 $RPM_BUILD_ROOT/usr/man/man1/

%files
/usr/bin/gfocustimer
/usr/man/man1/gfocustimer.1

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
