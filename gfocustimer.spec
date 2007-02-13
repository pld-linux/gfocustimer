Summary:	Prepare timesheet from X window usage
Summary(pl.UTF-8):	Aplikacja przygotowująca rozkład korzystania z okienek X
Vendor:		James Cameron
Name:		gfocustimer
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://quozl.us.netrek.org/gfocustimer/%{name}-%{version}.tar.gz
# Source0-md5:	e6d01e6b8edcf33d9860a6b23a393a07
Patch0:		%{name}-DESTDIR.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
URL:		http://quozl.us.netrek.org/gfocustimer/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gfocustimer captures information about which windows you are spending
your time in, to assist with personal scheduling and preparing
timesheets. 

gfocustimer displays a list of chargable tasks which con- sist of an
entry name and the time spent on the task. It can be used in a manual
mode, where the user selects a new entry, or in a semi-automatic focus
watching mode, where the user connects windows on screen to tasks.

%description -l pl.UTF-8
gfocustimer zbiera informacje o oknach, przy których spędza się czas,
by pomóc w przygotowaniu osobistego terminarza. gfocustimer wyświetla
listę wykonanych zadań, która składa się z nazwy oraz czasu spędzonego
przy danym zadaniu. Można go użyć w trybie ręcznym, w którym
użytkownik wybiera nowe zadanie, lub też w półautomatycznym trybie
oglądania, kiedy użytkownik łączy okna wyświetlane na ekranie z
zadaniami.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gfocustimer
%{_mandir}/man1/gfocustimer.1*
