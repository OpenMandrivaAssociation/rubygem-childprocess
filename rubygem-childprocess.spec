%define gemname childprocess

%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}
%define rubyabi 1.8

Summary: A simple and reliable solution for controlling external programs running in the background
Name: rubygem-%{gemname}
Version: 0.3.0
Release: 1
Group: Development/Ruby 
License: MIT
URL: http://github.com/jarib/childprocess
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby-RubyGems
Requires: ruby
Requires: rubygem(ffi) => 1.0.6
Requires: rubygem(ffi) < 1.1
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: ruby-RubyGems
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
This gem aims at being a simple and reliable solution for controlling external
programs running in the background on any Ruby / OS combination.


%package doc
Summary: Documentation for %{name}
Group: Development/Ruby
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}


%prep
%setup -q -c -T
mkdir -p .%{gemdir}
gem install --local --install-dir .%{gemdir} --force %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gemdir}
cp -a .%{gemdir}/* %{buildroot}%{gemdir}/
rm -f %{buildroot}%{geminstdir}/.document %{buildroot}%{geminstdir}/.gitignore
rm -f %{buildroot}%{geminstdir}/.rspec %{buildroot}%{geminstdir}/Rakefile
rm -f %{buildroot}%{geminstdir}/childprocess.gemspec
rm -f %{buildroot}%{geminstdir}/Gemfile
chmod 644 %{buildroot}%{geminstdir}/lib/childprocess/jruby/process.rb
chmod 644 %{buildroot}%{geminstdir}/lib/childprocess/windows/process.rb
chmod 644 %{buildroot}%{geminstdir}/spec/*.rb


%files
%dir %{geminstdir}
%doc %{geminstdir}/LICENSE
%doc %{geminstdir}/README.md
%{geminstdir}/lib
%{geminstdir}/.travis.yml
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/spec
