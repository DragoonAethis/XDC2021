import obspython as S
import datetime

# {}  ~/dayN  $ next-talk

class ClockUpdater:
    def __init__(self):
        self.source_name = None
        self.template = None
        self.prev_text = None
        self.running = False

    def print_status(self):
        print(f"Running: {self.running}, template: {self.template}, target: {self.source_name}")

    def update_text(self):
        if not self.running or self.source_name is None or self.template is None:
            return

        try:
            clock = datetime.datetime.now().strftime("%H:%M")
            text = self.template.format(clock)
        except:
            text = "Template error!"

        if self.prev_text == text:
            return  # Don't set the text on each frame!

        print(f"setting text to {text}")

        source = S.obs_get_source_by_name(self.source_name)
        if source is not None:
            settings = S.obs_data_create()
            S.obs_data_set_string(settings, "text", text)
            S.obs_source_update(source, settings)
            S.obs_data_release(settings)
            S.obs_source_release(source)
            self.prev_text = text


updater = ClockUpdater()


def script_load(settings):
    updater.template = S.obs_data_get_string(settings, "template")
    updater.source_name = S.obs_data_get_string(settings, "target")
    updater.print_status()


def script_tick(seconds):
    updater.update_text()


def text_changed(props, prop, settings):
    updater.template = S.obs_data_get_string(settings, "template")
    updater.print_status()


def target_changed(props, prop, settings):
    updater.source_name = S.obs_data_get_string(settings, "target")
    updater.print_status()


def button_clicked(what, ever):
    updater.running = not updater.running
    updater.print_status()


def script_properties():
    props = S.obs_properties_create()

    text = S.obs_properties_add_text(props, "template", "Text", S.OBS_TEXT_DEFAULT)
    S.obs_property_set_modified_callback(text, text_changed)

    target = S.obs_properties_add_list(props, "target", "Target",
                                       S.OBS_COMBO_TYPE_LIST, S.OBS_COMBO_FORMAT_STRING)
    S.obs_property_set_modified_callback(target, target_changed)

    btn = S.obs_properties_add_button(props, "start_stop", "Start/Stop", button_clicked)

    sources = S.obs_enum_sources()
    if sources is not None:
        for source in sources:
            source_id = S.obs_source_get_unversioned_id(source)
            if source_id == "text_gdiplus" or source_id == "text_ft2_source":
                name = S.obs_source_get_name(source)
                S.obs_property_list_add_string(target, name, name)

        S.source_list_release(sources)

    return props
