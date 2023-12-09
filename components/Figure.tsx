import * as React from "react";
import Box from "@mui/material/Box";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import Typography from "@mui/material/Typography";
import CardMedia from "@mui/material/CardMedia";
import Grid from "@mui/material/Grid";

interface Props {
  title: string;
  url: string;
  size:number
}

export default function Figure({ title, url,size }: Props) {
  return (
    <Box sx={{ mt: 5 }}>
      <Card variant="outlined">
        <CardContent>
          <Grid
            container
            spacing={4}
            direction="row"
            justifyContent="center"
            alignItems="center"
          >
            <Grid item xs={size}>
              <CardMedia component="img" image={url} alt="Paella dish" />
            </Grid>
          </Grid>
          <Box sx={{ mt: 5 }}>
            <Typography variant="subtitle2" align="center">
              {title}
            </Typography>
          </Box>
        </CardContent>
      </Card>
    </Box>
  );
}
