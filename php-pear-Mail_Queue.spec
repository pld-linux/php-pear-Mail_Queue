%include	/usr/lib/rpm/macros.php
%define		_class		Mail
%define		_subclass	Queue
%define		_status		stable

%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - put mails in queue and send them later in background
Summary(pl.UTF-8):	%{_pearname} - ustawianie poczty w kolejce i późniejsze jej wysyłanie
Name:		php-pear-%{_pearname}
Version:	1.1.3
Release:	5
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	e1eae2fd188f1926a83b97cdcf0c239e
URL:		http://pear.php.net/package/Mail_Queue/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-Mail
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Class for handle mail queue managment. Wrapper for PEAR::Mail and
PEAR::DB. Could load, save and send saved mails in background and also
backup some mails. Mail queue class put mails in a temporary container
waiting to be fed to the MTA (Mail Transport Agent) and send them
later (eg. every few minutes) by crontab or in other way.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Klasa ta potrafi obsługiwać kolejki poczty. Jest to wrapper na
PEAR::Mail i PEAR::DB. Może ładować, zapisywać oraz wysyłać pocztę w
tle, a także robić backup niektórych maili. Maile są umieszczane w
tymczasowym kontenerze czekając na wysłanie do MTA (Mail Transport
Agent) i są wysyłane później (np. co kilka minut) przez crontaba lub w
inny sposób.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
