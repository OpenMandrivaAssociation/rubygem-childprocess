# Generated from childprocess-0.3.0.gem by gem2rpm5 0.6.5 -*- rpm-spec -*-
%define	rbname	childprocess
%define	desc	A simple and reliable solution for controlling external programs running in the background

Summary:	%{desc}
Name:		rubygem-%{rbname}

Version:	0.3.0
Release:	2
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://github.com/jarib/childprocess
Source0:	http://gems.rubyforge.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
This gem aims at being a simple and reliable solution for controlling external
programs running in the background on any Ruby / OS combination.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build

%install
%gem_install

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/childprocess
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/childprocess/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/childprocess/jruby
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/childprocess/jruby/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/childprocess/tools
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/childprocess/tools/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/childprocess/unix
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/childprocess/unix/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/childprocess/unix/platform
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/childprocess/unix/platform/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/childprocess/windows
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/childprocess/windows/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%{ruby_gemdir}/doc/%{rbname}-%{version}


%changelog
* Wed Feb 15 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.3.0-2
+ Revision: 774161
- mass rebuild of ruby packages against ruby 1.9.1

* Tue Jan 24 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.3.0-1
+ Revision: 767838
- files section rewritten
- version update 0.3.0

* Wed Sep 07 2011 Alexander Barakin <abarakin@mandriva.org> 0.2.0-1
+ Revision: 698570
- imported package rubygem-childprocess

