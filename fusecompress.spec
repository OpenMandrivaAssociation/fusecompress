# These need from git tarball.
%define gitrel 39
%define downloadcode  913897f

%define build_bzip2 1
%define build_lzma 1
%define build_lzo 1
%define build_zlib 1

%{?_with_bzip2: %{expand: %%global build_bzip2 1}}
%{?_without_bzip2: %{expand: %%global build_bzip2 0}}
%{?_with_lzma: %{expand: %%global build_lzma 1}}
%{?_without_lzma: %{expand: %%global build_lzma 0}}
%{?_with_lzo: %{expand: %%global build_lzo 1}}
%{?_without_lzo: %{expand: %%global build_lzo 0}}
%{?_with_zlib: %{expand: %%global build_zlib 1}}
%{?_without_zlib: %{expand: %%global build_zlib 0}}

Summary:	Provides a mountable Linux filesystem which transparently compress its content
Name:		fusecompress
Version:	2.6
Release:	1.0.git.20110205.3
License:	GPL
Group:		System/Kernel and hardware
URL:		http://miio.net/wordpress/projects/fusecompress/
# Please add comment with the right url/downloadpage.
Source0:	http://download.github.com/tex-%{name}-%{version}-%{gitrel}-g%{downloadcode}.tar.gz

%if %{build_bzip2}
BuildRequires:	libbzip2-devel
%endif
%if %{build_lzma}
Requires:	xz
BuildRequires:	liblzma-devel
%endif
%if %{build_lzo}
BuildRequires:	liblzo-devel
%endif
%if %{build_zlib}
BuildRequires:	zlib-devel
%endif
BuildRequires:	boost-devel
BuildRequires:	fuse-devel
BuildRequires:	libmagic-devel
Requires:	fuse

%description
FuseCompress provides a mountable Linux file system which transparently compress its content.
Files stored in this file system are compressed on the fly and Fuse allows to create a transparent interface between compressed files and user applications.
FuseCompress currently supports these compression methods:
- bzip2 compression
- lzma compression
- lzo2 compression
- zlib compression
- none compression

%prep
%setup -q -n tex-%{name}-%{downloadcode}

%build
%configure2_5x \
%if %{build_bzip2}
	--with-bz2 \
%endif
%if %{build_lzma}
	--with-lzma \
%endif
%if %{build_lzo}
	--with-lzo2 \
%endif
%if %{build_zlib}
	--with-z \
%endif
	--with-boost=%{_prefix} \
	--with-boost-libdir=%{_libdir}
%make

%install
%makeinstall_std
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_bindir}/*
%{_mandir}/man1/%{name}*

