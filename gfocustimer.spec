Summary:	Prepare timesheet from X window usage
Vendor:		James Cameron
Name:		gfocustimer
Version:	0.4
Release:	1
License:	GPL
Group:		Applications/Productivity
Source:		gfocustimer-0.4.tar.gz
URL:		http://quozl.us.netrek.org/gfocustimer/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gfocustimer  captures  information about which windows you
are  spending  your  time  in,  to  assist  with  personal
scheduling and preparing timesheets.

gfocustimer  displays a list of chargable tasks which con-
sist of an entry name and the time spent on the task.   It
can be used in a manual mode, where the user selects a new
entry, or in a semi-automatic focus watching  mode,  where
the user connects windows on screen to tasks.

%description -l pl
gfocustimer zbiera informacje o oknach, przy kt�rych spedza si� czas,
by pom�c w przygotowaniu osobistego terminarza.
gfocustimer wy�wietla list� wykonanych zada�, kt�ra sk�ada si� z
nazwy oraz czasu sp�dzonego przy danym zadaniu. Mo�na go u�y�
w trybie r�cznym, w kt�rym u�ytkownik wybiera nowe zadanie, lub 
te� w p�automatycznym trybie ogl�dania, kiedy u�ytkownik ��czy 
okna wyswietlane na ekranie z zadaniami.

%prep
%setup -q

%build
pwd
./configure --prefix=/usr
make

%install
install -d $RPM_BUILD_ROOT/usr/bin/
install src/gfocustimer $RPM_BUILD_ROOT/usr/bin/
install -d $RPM_BUILD_ROOT/usr/man/man1/
install gfocustimer.1 $RPM_BUILD_ROOT/usr/man/man1/

%files
/usr/bin/gfocustimer
/usr/man/man1/gfocustimer.1

%clean
rm -rf $RPM_BUILD_ROOT
