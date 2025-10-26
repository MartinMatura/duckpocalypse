import * as React from "react";
import IconButton from "@mui/material/IconButton";


export default function DuckButton() {
    return (   
        <IconButton
            onClick = {() => alert("Quack!")}
            sx = {{
                padding: 0,
                borderRadius: 2,
                "&: hover image": {opacity: 0.8},
            }}
        >
            <img
                src="/duck.jpeg"
                alt="Duck"
                style={{
                    width: 60,
                    height: 60,
                    borderRadius: "8px",
                }}
            />
        </IconButton>
    );
}