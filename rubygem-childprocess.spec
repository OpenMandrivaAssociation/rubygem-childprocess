%define rbname childprocess

Summary:	Control external programs running in the background
Name:		rubygem-%{rbname}
Version:	0.5.3
Release:	1
License:	MIT
Group:		Development/Ruby
Url:		https://rubygems.org/gems/%{rbname}
Source0:	https://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems
BuildArch:	noarch

%description
This gem aims at being a simple and reliable solution for controlling external
programs running in the background on any Ruby / OS combination.

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

#----------------------------------------------------------------------------

%package doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name} = %{EVRD}

%description doc
Documents, RDoc & RI documentation for %{name}.

%files doc
%{ruby_gemdir}/doc/%{rbname}-%{version}

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%gem_build

%install
%gem_install

