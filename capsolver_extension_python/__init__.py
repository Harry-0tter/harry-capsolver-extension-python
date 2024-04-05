from chrome_extension_python import Extension


class Capsolver(Extension):
    def __init__(self, api_key, blacklist_enabled=False, blacklist_urls=None, app_id=None):
        super().__init__(
            extension_id="pgojnojmmhpofjgdmaebadhbocahppod",
            extension_name="capsolver",
            api_key=api_key,
            app_id=app_id,
        )
        self.blacklist_enabled = blacklist_enabled
        self.blacklist_urls = blacklist_urls or []

    def update_files(self, api_key, app_id):
        def update_js_contents(content):
            to_replace = "return e.defaultConfig"
            app_id_str = f", appId: '{app_id}'" if app_id else ""
            replacement = (
                f"return {{ ...e.defaultConfig, apiKey: '{api_key}'{app_id_str} }}"
            )
            content = content.replace(to_replace, replacement)

            if self.blacklist_enabled:
                content = content.replace("enabledForBlacklistControl:!1", "enabledForBlacklistControl:!0")
                content = content.replace("blackUrlList:[]", f"blackUrlList:{self.blacklist_urls}")

            return content

        for file in self.get_js_files():
            file.update_contents(update_js_contents)

        def update_config_contents(content):
            key_replaced = content.replace("apiKey: '',", f"apiKey: '{api_key}',")
            if app_id:
                key_replaced = key_replaced.replace("appId: '',", f"appId: '{app_id}',")

            if self.blacklist_enabled:
                key_replaced = key_replaced.replace("enabledForBlacklistControl: false,",
                                                    "enabledForBlacklistControl: true,")
                key_replaced = key_replaced.replace("blackUrlList: [],", f"blackUrlList: {self.blacklist_urls},")

            return key_replaced

        self.get_file("/assets/config.js").update_contents(update_config_contents)