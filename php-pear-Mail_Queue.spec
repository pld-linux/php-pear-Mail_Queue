%include	/usr/lib/rpm/macros.php
%define		_class		Mail
%define		_subclass	Queue
%define		_status		stable

%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - put mails in queue and send them later in background
Summary(pl):	%{_pearname} - ustawia pocztê w kolejce i wysy³a j± pó¼niej
Name:		php-pear-%{_pearname}
Version:	1.1.2
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	1a19447381ac3cc3a2bb6894cea59765
URL:		http://pear.php.net/package/Mail_Queue/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Class for handle mail queue managment. Wrapper for PEAR::Mail and
PEAR::DB. Could load, save and send saved mails in background and also
backup some mails. Mail queue class put mails in a temporary container
waiting to be fed to the MTA (Mail Transport Agent) and send them
later (eg. every few minutes) by crontab or in other way.

In PEAR status of this package is: %{_status}.

%description -l pl
Klasa ta potrafi obs³ugiwaæ kolejki poczty. Jest to wrapper na
PEAR::Mail i PEAR::DB. Mo¿e ³adowaæ, zapisywaæ oraz wysy³aæ pocztê w
tle, a tak¿e robiæ backup niektórych maili. Maile s± umieszczane w
tymczasowym kontenerze czekaj±c na wys³anie do MTA (Mail Transport
Agent) i s± wysy³ane pó¼niej (np. co kilka minut) przez crontaba lub w
inny sposób.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c
cd %{_pearname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{version}/*.php	$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/
install %{_pearname}-%{version}/%{_subclass}/*.php	$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/docs/*
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
