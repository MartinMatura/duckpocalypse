import AppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import IconButton from "@mui/material/IconButton";
import MenuIcon from "@mui/icons-material/Menu";
import DuckButton from "./DuckButton.jsx";
import * as React from "react";
import Drawer from "@mui/material/Drawer";
import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import ListItemText from "@mui/material/ListItemText";
import TextField from "@mui/material/TextField";
import Divider from "@mui/material/Divider";

export default function Header() {
    const [open, setOpen] = React.useState(false);
    const [search, setSearch] = React.useState("");

    const toggleDrawer = (state) => () => {
        setOpen(state);
    };

    const handleSearchChange = (e) => {
        setSearch(e.target.value);
    };

    const handleSearchSubmit = (e) => {
        e.preventDefault();
        alert(
            "Why are you searching things? You should be focusing on duck domination??"
        );
        setSearch("");
    }

    return (
        <>
        <AppBar 
            position="static"
            elevation={0}
            sx={{
                backgroundColor: '#f9f4c0ff',
                color: 'black'
            }}>
            <Toolbar>
                <IconButton
                    size="large"
                    edge="start"
                    color="inherit"
                    aria-label="menu"
                    sx={{ mr:90 }}
                    onClick={toggleDrawer(true)}
                >
                    <MenuIcon />
                </IconButton>

                <Typography
                    variant="h4"
                    component="div"
                    sx={{ textAlign: "center",
                        fontWeight: "bold",
                     }}
                >
                    Duckpocalypse*
                </Typography>
                <div
                    style={{
                        position: "absolute",
                        right: 16,
                    }}
                >
                <DuckButton />
                </div>
            </Toolbar>
        </AppBar>

        <Drawer
            anchor="left"
            open={open}
            onClose={toggleDrawer(false)}
        > 
        <List sx={{ width: 250, p: 2}}>
            <Typography variant="h6" sx={{ mb: 1 }}>
                Taskbar
            </Typography>
            <Divider sx={{ mb: 2 }} />

            <form onSubmit={handleSearchSubmit}>
                <TextField
                    label="Search the web..."
                    variant="outlined"
                    fullWidth
                    size="small"
                    value={search}
                    onChange={handleSearchChange}
                />
            </form>
            <ListItem sx={{ flexDirection: "column", alignItems: "center", mt: 2}}>
                <ListItemText
                    primary="(Nothing to see here, human...)"
                    sx={{ textAlign: "center", mb: 1 }}
                />
                <img
                    src="/dancing_duck.webp"
                    alt="Dancing duck"
                    className="w-32 h-auto rounded-lg shadow-md"
                />
            </ListItem>
        </List>  
        </Drawer>
    </>
    );
}