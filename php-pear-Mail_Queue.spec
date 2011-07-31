%include	/usr/lib/rpm/macros.php
%define		_status		stable
%define		_pearname	Mail_Queue
Summary:	%{_pearname} - put mails in queue and send them later in background
Summary(pl.UTF-8):	%{_pearname} - ustawianie poczty w kolejce i późniejsze jej wysyłanie
Name:		php-pear-%{_pearname}
Version:	1.2.7
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	4e4ebb51415060355b50da088eb94f4c
URL:		http://pear.php.net/package/Mail_Queue/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-Mail
Requires:	php-pear-Mail_Mime
Suggests:	php-creole
Suggests:	php-jargon
Suggests:	php-pear-DB
Suggests:	php-pear-MDB
Suggests:	php-pear-MDB2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	pear(creole/Creole.php) pear(DB.*) pear(MDB.*) pear(MDB2.*) pear(jargon.*)

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
cat > optional-packages.txt << 'EOF'
php-pear-%{_pearname} can optionally use package php-creole
EOF

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/%{_pearname}/docs/* optional-packages.txt
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Mail/Queue.php
%{php_pear_dir}/Mail/Queue
