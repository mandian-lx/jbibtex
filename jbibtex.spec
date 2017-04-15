%{?_javapackages_macros:%_javapackages_macros}

Summary:	Java BibTeX and LaTeX parser and formatter library
Name:		jbibtex
Version:	1.0.15
Release:	1
License:	BSD
Group:		Development/Java
URL:		https://github.com/jbibtex/%{name}
Source0:	https://github.com/jbibtex/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# Revert https://github.com/jbibtex/jbibtex/commit/d9018b324785abe96663f256661de9e5173b7ab4.patch
Patch0:		%{name}-1.0.15-javacc5.patch
BuildArch:	noarch

BuildRequires:	jpackage-utils
BuildRequires:	java-headless
BuildRequires:	maven-local
BuildRequires:	mvn(junit:junit)
BuildRequires:	mvn(org.codehaus.mojo:javacc-maven-plugin)

%description
Java BibTeX and LaTeX parser and formatter library.

%files -f .mfiles
%doc README.md
%doc LICENSE.txt

#----------------------------------------------------------------------------

%package	javadoc
Summary:	Javadoc for %{name}
Group:		Documentation

%description javadoc
API documentation for %{name}.

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

#----------------------------------------------------------------------------

%prep
%setup -q 

# Delete prebuild JARs and classes
find . -name "*.jar" -delete
find . -name "*.class" -delete

# Apply all patches
%patch0 -p1 -b .orig

# fix jar-not-indexed warning
%pom_add_plugin :maven-jar-plugin . "<configuration>
	<archive>
		<index>true</index>
	</archive>
</configuration>"

%build
%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

