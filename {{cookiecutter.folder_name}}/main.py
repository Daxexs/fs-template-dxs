from pathlib import Path

import flet_easy as fs
from core.config import ConfigApp

app = fs.FletEasy(
    route_init="/home",
    path_views=Path(__file__).parent / "views"
    )

# We load the application configuration.
ConfigApp(app)

# We run the application
app.run()
