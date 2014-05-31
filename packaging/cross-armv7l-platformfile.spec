# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.22git
# 
# >> macros
# << macros

Name:       cross-armv7l-platformfile
Summary:    Install armv7l /etc/rpm/platform file
Version:    0.0.1
Release:    1
Group:      Development/Tools
License:    GPLv2
Source100:  cross-armv7l-platformfile.yaml
Source1:    platform
BuildArch:  noarch
%description
Package to make rpm-x86 understand the build chroot is for armv7l



%prep
# >> setup
cp %{SOURCE1} .
# << setup

%build
# >> build pre
# << build pre



# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
mkdir -p %{buildroot}/etc/rpm
cp platform %{buildroot}/etc/rpm
# << install pre

# >> install post
# << install post






%files
%defattr(-,root,root,-)
/etc/rpm/platform
# >> files
# << files


