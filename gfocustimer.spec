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
gfocustimer zbiera informacje o oknach, przy których spedza siê czas,
by pomóc w przygotowaniu osobistego terminarza.
gfocustimer wy¶wietla listê wykonanych zadañ, która sk³ada siê z
nazwy oraz czasu spêdzonego przy danym zadaniu. Mo¿na go u¿yæ
w trybie rêcznym, w którym u¿ytkownik wybiera nowe zadanie, lub 
te¿ w pó³automatycznym trybie ogl±dania, kiedy u¿ytkownik ³±czy 
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
