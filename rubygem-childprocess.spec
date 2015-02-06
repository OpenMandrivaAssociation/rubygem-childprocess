%define rbname childprocess

Summary:	Control external programs running in the background
Name:		rubygem-%{rbname}
Version:	0.5.3
Release:	2
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
%dir %{gem_dir}/gems/%{rbname}-%{version}
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib
%{gem_dir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/childprocess
%{gem_dir}/gems/%{rbname}-%{version}/lib/childprocess/*.rb
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/childprocess/jruby
%{gem_dir}/gems/%{rbname}-%{version}/lib/childprocess/jruby/*.rb
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/childprocess/tools
%{gem_dir}/gems/%{rbname}-%{version}/lib/childprocess/tools/*.rb
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/childprocess/unix
%{gem_dir}/gems/%{rbname}-%{version}/lib/childprocess/unix/*.rb
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/childprocess/unix/platform
%{gem_dir}/gems/%{rbname}-%{version}/lib/childprocess/unix/platform/*.rb
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/childprocess/windows
%{gem_dir}/gems/%{rbname}-%{version}/lib/childprocess/windows/*.rb
%{gem_dir}/specifications/%{rbname}-%{version}.gemspec

#----------------------------------------------------------------------------

%package doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name} = %{EVRD}

%description doc
Documents, RDoc & RI documentation for %{name}.

%files doc
%{gem_dir}/doc/%{rbname}-%{version}

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%gem_build

%install
%gem_install

