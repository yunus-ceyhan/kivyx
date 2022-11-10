
from kivy.factory import Factory

register = Factory.register
register("XBoxLayout", module="kivyx.boxlayout")
register("XButton", module="kivyx.button")
register("XIconButton", module="kivyx.button")
register("XCard", module="kivyx.card")
register("XFloatLayout", module="kivyx.floatlayout")
register("XGridLayout(", module="kivyx.gridlayout")
register("XIcon", module="kivyx.icon")
register("XImage", module="kivyx.image")
register("XGifImage", module="kivyx.image")
register("XUrlImage", module="kivyx.image")
register("XLabel", module="kivyx.label")
register("XLinex", module="kivyx.line")
register("XLiney", module="kivyx.line")
register("XScreen", module="kivyx.screen")
register("XSpinner", module="kivyx.spinner")
register("XToolbar", module="kivyx.toolbar")
register("XSearchbar", module="kivyx.toolbar")
register("XAppToolbar", module="kivyx.toolbar")
register("XAppSearchbar", module="kivyx.toolbar")

register("XWidget", module="kivyx.widget")
register("XBotnavItem", module="kivyx.botnav")
register("XBotnav", module="kivyx.botnav")
register("XSidenav", module="kivyx.sidenav")
register("XMenu", module="kivyx.menu")
register("XDotMenu", module="kivyx.menu")
register("XDotItem", module="kivyx.menu")

register("XFab", module="kivyx.floating")
register("XActionFab", module="kivyx.floating")

register("XSwitch", module="kivyx.selection")

register("XTabPanel", module="kivyx.tab")
register("XTabItem", module="kivyx.tab")

register("XSegmentTab", module="kivyx.segmenttab")
register("XSegmentItem", module="kivyx.segmenttab")


register("ETabPanel", module="kivyx.editor.etab")
register("ETabItem", module="kivyx.editor.etab")

register("XListItem", module="kivyx.list")
register("XIconListItem", module="kivyx.list")
register("XImageListItem", module="kivyx.list")
register("XTwoIconListItem", module="kivyx.list")
register("XCustomListItem", module="kivyx.list")

register("XBottomSheet", module="kivyx.bottomsheet")
register("XBottomSheetContent", module="kivyx.bottomsheet")

register("XDialog", module="kivyx.dialog")
register("XDialogContent", module="kivyx.dialog")
register("XDialogButton", module="kivyx.dialog")

register("XSlider", module="kivyx.slider")
register("XProgress", module="kivyx.progress")
register("XCProgress", module="kivyx.progress")

register("XRcBoxList", module="kivyx.rclist")
register("XRcGridList", module="kivyx.rclist")

register("XChip", module="kivyx.chip")

register("XSegmentControl", module="kivyx.segmentcontrol")
register("XSegmentTextItem", module="kivyx.segmentcontrol")
register("XSegmentIconItem", module="kivyx.segmentcontrol")

register("XInput", module="kivyx.input")
register("XTextInput", module="kivyx.input")
register("XCodeInput", module="kivyx.input")
