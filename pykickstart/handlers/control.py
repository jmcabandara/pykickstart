#
# Chris Lumens <clumens@redhat.com>
#
# Copyright 2007 Red Hat, Inc.
#
# This software may be freely redistributed under the terms of the GNU
# general public license.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#
from pykickstart.version import *
from pykickstart.commands import *

commandMap = {
    FC3: {
        "auth": authconfig.FC3_Authconfig,
        "authconfig": authconfig.FC3_Authconfig,
        "autopart": autopart.FC3_AutoPart,
        "autostep": autostep.FC3_AutoStep,
        "bootloader": bootloader.FC3_Bootloader,
        "cdrom": method.FC3_Method,
        "clearpart": clearpart.FC3_ClearPart,
        "cmdline": displaymode.FC3_DisplayMode,
        "device": device.FC3_Device,
        "deviceprobe": deviceprobe.FC3_DeviceProbe,
        "driverdisk": driverdisk.FC3_DriverDisk,
        "firewall": firewall.FC3_Firewall,
        "firstboot": firstboot.FC3_Firstboot,
        "graphical": displaymode.FC3_DisplayMode,
        "halt": reboot.FC3_Reboot,
        "harddrive": method.FC3_Method,
        "ignoredisk": ignoredisk.FC3_IgnoreDisk,
        "install": upgrade.FC3_Upgrade,
        "interactive": interactive.FC3_Interactive,
        "keyboard": keyboard.FC3_Keyboard,
        "lang": lang.FC3_Lang,
        "langsupport": langsupport.FC3_LangSupport,
        "lilo": bootloader.FC3_Bootloader,
        "lilocheck": lilocheck.FC3_LiloCheck,
        "logvol": logvol.FC3_LogVol,
        "monitor": monitor.FC3_Monitor,
        "mouse": mouse.FC3_Mouse,
        "network": network.FC3_Network,
        "nfs": method.FC3_Method,
        "part": partition.FC3_Partition,
        "partition": partition.FC3_Partition,
        "poweroff": reboot.FC3_Reboot,
        "raid": raid.FC3_Raid,
        "reboot": reboot.FC3_Reboot,
        "rootpw": rootpw.FC3_RootPw,
        "selinux": selinux.FC3_SELinux,
        "shutdown": reboot.FC3_Reboot,
        "skipx": skipx.FC3_SkipX,
        "text": displaymode.FC3_DisplayMode,
        "timezone": timezone.FC3_Timezone,
        "upgrade": upgrade.FC3_Upgrade,
        "url": method.FC3_Method,
        "vnc": vnc.FC3_Vnc,
        "volgroup": volgroup.FC3_VolGroup,
        "xconfig": xconfig.FC3_XConfig,
        "zerombr": zerombr.FC3_ZeroMbr,
        "zfcp": zfcp.FC3_ZFCP,
    },

    # based on fc3
    FC4: {
        "auth": authconfig.FC3_Authconfig,
        "authconfig": authconfig.FC3_Authconfig,
        "autopart": autopart.FC3_AutoPart,
        "autostep": autostep.FC3_AutoStep,
        "bootloader": bootloader.FC4_Bootloader,
        "cdrom": method.FC3_Method,
        "clearpart": clearpart.FC3_ClearPart,
        "cmdline": displaymode.FC3_DisplayMode,
        "device": device.FC3_Device,
        "deviceprobe": deviceprobe.FC3_DeviceProbe,
        "driverdisk": driverdisk.FC3_DriverDisk,
        "firewall": firewall.FC3_Firewall,
        "firstboot": firstboot.FC3_Firstboot,
        "graphical": displaymode.FC3_DisplayMode,
        "halt": reboot.FC3_Reboot,
        "harddrive": method.FC3_Method,
        "ignoredisk": ignoredisk.FC3_IgnoreDisk,
        "install": upgrade.FC3_Upgrade,
        "interactive": interactive.FC3_Interactive,
        "keyboard": keyboard.FC3_Keyboard,
        "lang": lang.FC3_Lang,
        "langsupport": langsupport.FC3_LangSupport,
        "logvol": logvol.FC4_LogVol,
        "mediacheck": mediacheck.FC4_MediaCheck,
        "monitor": monitor.FC3_Monitor,
        "mouse": mouse.FC3_Mouse,
        "network": network.FC4_Network,
        "nfs": method.FC3_Method,
        "part": partition.FC4_Partition,
        "partition": partition.FC4_Partition,
        "poweroff": reboot.FC3_Reboot,
        "raid": raid.FC4_Raid,
        "reboot": reboot.FC3_Reboot,
        "rootpw": rootpw.FC3_RootPw,
        "selinux": selinux.FC3_SELinux,
        "shutdown": reboot.FC3_Reboot,
        "skipx": skipx.FC3_SkipX,
        "text": displaymode.FC3_DisplayMode,
        "timezone": timezone.FC3_Timezone,
        "upgrade": upgrade.FC3_Upgrade,
        "url": method.FC3_Method,
        "vnc": vnc.FC3_Vnc,
        "volgroup": volgroup.FC3_VolGroup,
        "xconfig": xconfig.FC3_XConfig,
        "zerombr": zerombr.FC3_ZeroMbr,
        "zfcp": zfcp.FC3_ZFCP,
    },

    # based on fc4
    FC5: {
        "auth": authconfig.FC3_Authconfig,
        "authconfig": authconfig.FC3_Authconfig,
        "autopart": autopart.FC3_AutoPart,
        "autostep": autostep.FC3_AutoStep,
        "bootloader": bootloader.FC4_Bootloader,
        "cdrom": method.FC3_Method,
        "clearpart": clearpart.FC3_ClearPart,
        "cmdline": displaymode.FC3_DisplayMode,
        "device": device.FC3_Device,
        "deviceprobe": deviceprobe.FC3_DeviceProbe,
        "driverdisk": driverdisk.FC3_DriverDisk,
        "firewall": firewall.FC3_Firewall,
        "firstboot": firstboot.FC3_Firstboot,
        "graphical": displaymode.FC3_DisplayMode,
        "halt": reboot.FC3_Reboot,
        "harddrive": method.FC3_Method,
        "ignoredisk": ignoredisk.FC3_IgnoreDisk,
        "install": upgrade.FC3_Upgrade,
        "interactive": interactive.FC3_Interactive,
        "keyboard": keyboard.FC3_Keyboard,
        "lang": lang.FC3_Lang,
        "langsupport": langsupport.FC5_LangSupport,
        "logvol": logvol.FC4_LogVol,
        "mediacheck": mediacheck.FC4_MediaCheck,
        "monitor": monitor.FC3_Monitor,
        "mouse": mouse.FC3_Mouse,
        "network": network.FC4_Network,
        "nfs": method.FC3_Method,
        "part": partition.FC4_Partition,
        "partition": partition.FC4_Partition,
        "poweroff": reboot.FC3_Reboot,
        "raid": raid.FC5_Raid,
        "reboot": reboot.FC3_Reboot,
        "rootpw": rootpw.FC3_RootPw,
        "selinux": selinux.FC3_SELinux,
        "shutdown": reboot.FC3_Reboot,
        "skipx": skipx.FC3_SkipX,
        "text": displaymode.FC3_DisplayMode,
        "timezone": timezone.FC3_Timezone,
        "upgrade": upgrade.FC3_Upgrade,
        "url": method.FC3_Method,
        "vnc": vnc.FC3_Vnc,
        "volgroup": volgroup.FC3_VolGroup,
        "xconfig": xconfig.FC3_XConfig,
        "zerombr": zerombr.FC3_ZeroMbr,
        "zfcp": zfcp.FC3_ZFCP,
    },

    # based on fc5
    FC6: {
        "auth": authconfig.FC3_Authconfig,
        "authconfig": authconfig.FC3_Authconfig,
        "autopart": autopart.FC3_AutoPart,
        "autostep": autostep.FC3_AutoStep,
        "bootloader": bootloader.FC4_Bootloader,
        "cdrom": method.FC6_Method,
        "clearpart": clearpart.FC3_ClearPart,
        "cmdline": displaymode.FC3_DisplayMode,
        "device": device.FC3_Device,
        "deviceprobe": deviceprobe.FC3_DeviceProbe,
        "dmraid": dmraid.FC6_DmRaid,
        "driverdisk": driverdisk.FC3_DriverDisk,
        "firewall": firewall.FC3_Firewall,
        "firstboot": firstboot.FC3_Firstboot,
        "graphical": displaymode.FC3_DisplayMode,
        "halt": reboot.FC6_Reboot,
        "harddrive": method.FC6_Method,
        "ignoredisk": ignoredisk.FC3_IgnoreDisk,
        "install": upgrade.FC3_Upgrade,
        "interactive": interactive.FC3_Interactive,
        "iscsi": iscsi.FC6_Iscsi,
        "iscsiname": iscsiname.FC6_IscsiName,
        "keyboard": keyboard.FC3_Keyboard,
        "lang": lang.FC3_Lang,
        "langsupport": langsupport.FC5_LangSupport,
        "logging": logging.FC6_Logging,
        "logvol": logvol.FC4_LogVol,
        "mediacheck": mediacheck.FC4_MediaCheck,
        "monitor": monitor.FC6_Monitor,
        "mouse": mouse.FC3_Mouse,
        "multipath": multipath.FC6_MultiPath,
        "network": network.FC6_Network,
        "nfs": method.FC6_Method,
        "part": partition.FC4_Partition,
        "partition": partition.FC4_Partition,
        "poweroff": reboot.FC6_Reboot,
        "raid": raid.FC5_Raid,
        "reboot": reboot.FC6_Reboot,
        "repo": repo.FC6_Repo,
        "rootpw": rootpw.FC3_RootPw,
        "selinux": selinux.FC3_SELinux,
        "services": services.FC6_Services,
        "shutdown": reboot.FC6_Reboot,
        "skipx": skipx.FC3_SkipX,
        "text": displaymode.FC3_DisplayMode,
        "timezone": timezone.FC3_Timezone,
        "upgrade": upgrade.FC3_Upgrade,
        "user": user.FC6_User,
        "url": method.FC6_Method,
        "vnc": vnc.FC6_Vnc,
        "volgroup": volgroup.FC3_VolGroup,
        "xconfig": xconfig.FC6_XConfig,
        "zerombr": zerombr.FC3_ZeroMbr,
        "zfcp": zfcp.FC3_ZFCP,
    },

    # based on fc6
    F7: {
        "auth": authconfig.FC3_Authconfig,
        "authconfig": authconfig.FC3_Authconfig,
        "autopart": autopart.FC3_AutoPart,
        "autostep": autostep.FC3_AutoStep,
        "bootloader": bootloader.FC4_Bootloader,
        "cdrom": method.FC6_Method,
        "clearpart": clearpart.FC3_ClearPart,
        "cmdline": displaymode.FC3_DisplayMode,
        "device": device.FC3_Device,
        "deviceprobe": deviceprobe.FC3_DeviceProbe,
        "dmraid": dmraid.FC6_DmRaid,
        "driverdisk": driverdisk.FC3_DriverDisk,
        "firewall": firewall.FC3_Firewall,
        "firstboot": firstboot.FC3_Firstboot,
        "graphical": displaymode.FC3_DisplayMode,
        "halt": reboot.FC6_Reboot,
        "harddrive": method.FC6_Method,
        "ignoredisk": ignoredisk.FC3_IgnoreDisk,
        "install": upgrade.FC3_Upgrade,
        "interactive": interactive.FC3_Interactive,
        "iscsi": iscsi.FC6_Iscsi,
        "iscsiname": iscsiname.FC6_IscsiName,
        "key": key.F7_Key,
        "keyboard": keyboard.FC3_Keyboard,
        "lang": lang.FC3_Lang,
        "logging": logging.FC6_Logging,
        "logvol": logvol.FC4_LogVol,
        "mediacheck": mediacheck.FC4_MediaCheck,
        "monitor": monitor.FC6_Monitor,
        "multipath": multipath.FC6_MultiPath,
        "network": network.FC6_Network,
        "nfs": method.FC6_Method,
        "part": partition.FC4_Partition,
        "partition": partition.FC4_Partition,
        "poweroff": reboot.FC6_Reboot,
        "raid": raid.FC5_Raid,
        "reboot": reboot.FC6_Reboot,
        "repo": repo.FC6_Repo,
        "rootpw": rootpw.FC3_RootPw,
        "selinux": selinux.FC3_SELinux,
        "services": services.FC6_Services,
        "shutdown": reboot.FC6_Reboot,
        "skipx": skipx.FC3_SkipX,
        "text": displaymode.FC3_DisplayMode,
        "timezone": timezone.FC3_Timezone,
        "upgrade": upgrade.FC3_Upgrade,
        "url": method.FC6_Method,
        "user": user.FC6_User,
        "vnc": vnc.FC6_Vnc,
        "volgroup": volgroup.FC3_VolGroup,
        "xconfig": xconfig.FC6_XConfig,
        "zerombr": zerombr.FC3_ZeroMbr,
        "zfcp": zfcp.FC3_ZFCP,
    },

    # based on fc3
    RHEL4: {
        "auth": authconfig.FC3_Authconfig,
        "authconfig": authconfig.FC3_Authconfig,
        "autopart": autopart.FC3_AutoPart,
        "autostep": autostep.FC3_AutoStep,
        "bootloader": bootloader.FC3_Bootloader,
        "cdrom": method.FC3_Method,
        "clearpart": clearpart.FC3_ClearPart,
        "cmdline": displaymode.FC3_DisplayMode,
        "device": device.FC3_Device,
        "deviceprobe": deviceprobe.FC3_DeviceProbe,
        "driverdisk": driverdisk.FC3_DriverDisk,
        "firewall": firewall.FC3_Firewall,
        "firstboot": firstboot.FC3_Firstboot,
        "graphical": displaymode.FC3_DisplayMode,
        "halt": reboot.FC3_Reboot,
        "harddrive": method.FC3_Method,
        "ignoredisk": ignoredisk.FC3_IgnoreDisk,
        "install": upgrade.FC3_Upgrade,
        "interactive": interactive.FC3_Interactive,
        "keyboard": keyboard.FC3_Keyboard,
        "lang": lang.FC3_Lang,
        "langsupport": langsupport.FC3_LangSupport,
        "lilo": bootloader.FC3_Bootloader,
        "lilocheck": lilocheck.FC3_LiloCheck,
        "logvol": logvol.FC3_LogVol,
        "monitor": monitor.FC3_Monitor,
        "mouse": mouse.FC3_Mouse,
        "network": network.RHEL4_Network,
        "nfs": method.FC3_Method,
        "part": partition.FC3_Partition,
        "partition": partition.FC3_Partition,
        "poweroff": reboot.FC3_Reboot,
        "raid": raid.FC3_Raid,
        "reboot": reboot.FC3_Reboot,
        "rootpw": rootpw.FC3_RootPw,
        "selinux": selinux.FC3_SELinux,
        "shutdown": reboot.FC3_Reboot,
        "skipx": skipx.FC3_SkipX,
        "text": displaymode.FC3_DisplayMode,
        "timezone": timezone.FC3_Timezone,
        "upgrade": upgrade.FC3_Upgrade,
        "url": method.FC3_Method,
        "vnc": vnc.FC3_Vnc,
        "volgroup": volgroup.FC3_VolGroup,
        "xconfig": xconfig.FC3_XConfig,
        "zerombr": zerombr.FC3_ZeroMbr,
        "zfcp": zfcp.FC3_ZFCP,
    },

    # based on fc6
    RHEL5: {
        "auth": authconfig.FC3_Authconfig,
        "authconfig": authconfig.FC3_Authconfig,
        "autopart": autopart.FC3_AutoPart,
        "autostep": autostep.FC3_AutoStep,
        "bootloader": bootloader.FC4_Bootloader,
        "cdrom": method.FC6_Method,
        "clearpart": clearpart.FC3_ClearPart,
        "cmdline": displaymode.FC3_DisplayMode,
        "device": device.FC3_Device,
        "deviceprobe": deviceprobe.FC3_DeviceProbe,
        "dmraid": dmraid.FC6_DmRaid,
        "driverdisk": driverdisk.FC3_DriverDisk,
        "firewall": firewall.FC3_Firewall,
        "firstboot": firstboot.FC3_Firstboot,
        "graphical": displaymode.FC3_DisplayMode,
        "halt": reboot.FC6_Reboot,
        "harddrive": method.FC6_Method,
        "ignoredisk": ignoredisk.FC3_IgnoreDisk,
        "install": upgrade.FC3_Upgrade,
        "interactive": interactive.FC3_Interactive,
        "iscsi": iscsi.FC6_Iscsi,
        "iscsiname": iscsiname.FC6_IscsiName,
        "key": key.RHEL5_Key,
        "keyboard": keyboard.FC3_Keyboard,
        "lang": lang.FC3_Lang,
        "langsupport": langsupport.FC5_LangSupport,
        "logging": logging.FC6_Logging,
        "logvol": logvol.FC4_LogVol,
        "mediacheck": mediacheck.FC4_MediaCheck,
        "monitor": monitor.FC6_Monitor,
        "mouse": mouse.FC3_Mouse,
        "multipath": multipath.FC6_MultiPath,
        "network": network.FC6_Network,
        "nfs": method.FC6_Method,
        "part": partition.FC4_Partition,
        "partition": partition.FC4_Partition,
        "poweroff": reboot.FC6_Reboot,
        "raid": raid.FC5_Raid,
        "reboot": reboot.FC6_Reboot,
        "repo": repo.FC6_Repo,
        "rootpw": rootpw.FC3_RootPw,
        "services": services.FC6_Services,
        "selinux": selinux.FC3_SELinux,
        "shutdown": reboot.FC6_Reboot,
        "skipx": skipx.FC3_SkipX,
        "text": displaymode.FC3_DisplayMode,
        "timezone": timezone.FC3_Timezone,
        "upgrade": upgrade.FC3_Upgrade,
        "user": user.FC6_User,
        "url": method.FC6_Method,
        "vnc": vnc.FC6_Vnc,
        "volgroup": volgroup.FC3_VolGroup,
        "xconfig": xconfig.FC6_XConfig,
        "zerombr": zerombr.FC3_ZeroMbr,
        "zfcp": zfcp.FC3_ZFCP,
    }
}