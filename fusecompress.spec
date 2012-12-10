# These need from git tarball.
%define gitrel		41
%define downloadcode	4b43418

%define build_bzip2	1
%define build_lzma	1
%define build_lzo	1
%define build_zlib	1

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
Release:	2.%{gitrel}.1
License:	GPLv2
Group:		System/Kernel and hardware
URL:		http://miio.net/wordpress/projects/fusecompress/
# Please add comment with the right url/downloadpage.
Source0:	http://download.github.com/tex-%{name}-%{version}-%{gitrel}-g%{downloadcode}.tar.xz

%if %{build_bzip2}
BuildRequires:	bzip2-devel
%endif
%if %{build_lzma}
Requires:	xz
BuildRequires:	pkgconfig(liblzma)
%endif
%if %{build_lzo}
BuildRequires:	liblzo-devel
%endif
%if %{build_zlib}
BuildRequires:	pkgconfig(zlib)
%endif
BuildRequires:	boost-devel
BuildRequires:	magic-devel
BuildRequires:	pkgconfig(fuse)
Requires:	fuse

%description
FuseCompress provides a mountable Linux file system which transparently 
compress its content.  Files stored in this file system are compressed on the 
fly and Fuse allows to create a transparent interface between compressed files 
and user applications.

FuseCompress currently supports these compression methods:
- bzip2 compression
- lzma compression
- lzo2 compression
- zlib compression
- none compression

%prep
%setup -qn %{name}

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

%files
%doc AUTHORS COPYING README
%{_bindir}/*
%{_mandir}/man1/%{name}*



%changelog
* Sat Jun 09 2012 Matthew Dawkins <mattydaw@mandriva.org> 2.6-2.41.1
+ Revision: 804304
- new git snapshot 41
- cleaned up spec
- rebuild for boost libs
- cleaned up spec

* Mon Mar 14 2011 Funda Wang <fwang@mandriva.org> 2.6-1.0.git.20110205.2
+ Revision: 644477
- rebuild for new boost

* Mon Feb 28 2011 Lonyai Gergely <aleph@mandriva.org> 2.6-1.0.git.20110205.1
+ Revision: 641048
- Use only local assert.h and rlog/rlog.h.

* Wed Dec 01 2010 Funda Wang <fwang@mandriva.org> 0.6-1.0.git.20100822.3mdv2011.0
+ Revision: 604387
- rebuild for zlib

* Sat Nov 27 2010 Funda Wang <fwang@mandriva.org> 0.6-1.0.git.20100822.2mdv2011.0
+ Revision: 601651
- rebuild for py liblzma

* Mon Aug 23 2010 Funda Wang <fwang@mandriva.org> 0.6-1.0.git.20100822.1mdv2011.0
+ Revision: 572183
- new snapshot

* Wed Aug 04 2010 Funda Wang <fwang@mandriva.org> 0.6-1.0.git.20100107.6mdv2011.0
+ Revision: 565988
- rebuild for new boost

* Sat Feb 27 2010 Funda Wang <fwang@mandriva.org> 0.6-1.0.git.20100107.5mdv2010.1
+ Revision: 512264
- drop lib requries

  + Lonyai Gergely <aleph@mandriva.org>
    - Modify the description. I remove the conditions from it therefore they add unnessesary new line into the text.

* Mon Feb 08 2010 Anssi Hannula <anssi@mandriva.org> 0.6-1.0.git.20100107.4mdv2010.1
+ Revision: 501882
- rebuild for new boost

* Thu Feb 04 2010 Funda Wang <fwang@mandriva.org> 0.6-1.0.git.20100107.3mdv2010.1
+ Revision: 500581
- drop ununsed requries, corresponding requires have been added by file dep

* Wed Feb 03 2010 Funda Wang <fwang@mandriva.org> 0.6-1.0.git.20100107.2mdv2010.1
+ Revision: 500078
- rebuild for new boost

* Wed Feb 03 2010 Lonyai Gergely <aleph@mandriva.org> 0.6-1.0.git.20100107.1mdv2010.1
+ Revision: 500001
- Update to January 07, 2010
- Fix dependency in x86_64
- Fix requires section to the older distributions

* Sat Dec 05 2009 Funda Wang <fwang@mandriva.org> 0.6-1.0.git.20091024.2mdv2010.1
+ Revision: 473888
- drop invalid lib request (already there through file dep)

* Mon Nov 30 2009 Lonyai Gergely <aleph@mandriva.org> 0.6-1.0.git.20091024.1mdv2010.1
+ Revision: 471744
- Fix x86_64 libs problem
- rebuild
- initial release
- import fusecompress


