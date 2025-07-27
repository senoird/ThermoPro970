"""Config flow for ThermoPro TP920."""
import voluptuous as vol
from homeassistant import config_entries
from .const import DOMAIN

class ThermoProTP920ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for ThermoPro TP920."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            return self.async_create_entry(title="ThermoPro TP920", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({vol.Required("address"): str}),
        )