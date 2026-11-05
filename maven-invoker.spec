Name:		maven-invoker
Version:	3.3.0
Release:	1
Summary:	Invoke Maven from Java
Group:		Development/Java
License:	ASL 2.0
URL:		https://maven.apache.org/shared/maven-invoker/
Source0:	https://github.com/apache/maven-invoker/archive/refs/tags/maven-invoker-%{version}.tar.gz
BuildArch:	noarch
# Literal, so the first rpmbuild -bs records them before sysjar is installed.
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildRequires:	maven-shared
BuildRequires:	maven-shared-utils
BuildRequires:	mvn(javax.inject:javax.inject)
BuildSystem:	maven
BuildOption(install):	--file-name %{name}

Obsoletes:	maven-shared-invoker < %{EVR}
Provides:	maven-shared-invoker = %{EVR}

%description
Runs a Maven build from Java and collects its result. Used by the
Maven Javadoc plugin to fork javadoc builds.

%prep
%autosetup -n maven-invoker-maven-invoker-%{version}

%files -f .mfiles
%doc README.md
