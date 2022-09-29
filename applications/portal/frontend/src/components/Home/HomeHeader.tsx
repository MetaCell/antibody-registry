import React, { useState, useEffect } from "react";
import useScrollTrigger from "@mui/material/useScrollTrigger";
import {
  AppBar,
  Box,
  Button,
  Container,
  Grid,
  Stack,
  Typography,
} from "@mui/material";
import { useTheme } from "@mui/material/styles";
import { AddAntibodyIcon, DownloadIcon } from "../icons";
import TableToolbar from "./TableToolbar";
import { getRecords } from "../../services/AntibodiesService";

interface Props {
  /**
   * Injected by the documentation to work in an iframe.
   * You won't need it on your project.
   */
  window?: () => Window;
  children: React.ReactElement;
}
const HideOnScroll = (props: Props) => {
  const { children } = props;

  const trigger = useScrollTrigger();

  return <Box display={trigger ? "none" : "block"}>{children}</Box>;
};

const HomeHeader = (props) => {
  const theme = useTheme();
  const [records, setRecords] = useState<number>();
  const { activeSelection, handleExport, showFilterMenu, activeTab } = props;

  const fetchRecords = () => {
    getRecords()
      .then((res) => {
        console.log("res: ",res);
        setRecords(res.total);
      }).catch((err) => {
        console.log("Error: ", err)
      })
  }
  useEffect(fetchRecords,[]);

  return (
    <Box>
      <AppBar elevation={0} sx={{ top: "4.5rem" }}>
        <Container maxWidth="xl">
          <Stack direction="column" spacing={1.5} mb={1} width="100%">
            <HideOnScroll>
              <Box display="flex" mt={6} justifyContent="space-between">
                <Box>
                  <Grid container columnSpacing={1.5} rowSpacing={1}>
                    <Grid item>
                      <Typography variant="h1" color="grey.700" align="left">
                        Antibody Registry <sub>beta</sub>
                      </Typography>
                    </Grid>
                    <Grid item display="flex" alignItems="center">
                      <Box
                        bgcolor="primary.main"
                        borderRadius={2}
                        py={0.25}
                        px={1.25}
                      >
                        <Typography
                          variant="h6"
                          color="common.white"
                          align="left"
                        >
                          {records} {records>1?"records":"record"}
                        </Typography>
                      </Box>
                    </Grid>
                    <Grid item xs={12}>
                      <Typography
                        variant="subtitle1"
                        color="grey.400"
                        align="left"
                      >
                        Last Updated: Friday, 15th July
                      </Typography>
                    </Grid>
                  </Grid>
                </Box>
                <Box>
                  <Stack direction="row" spacing={1.5}>
                    <Button
                      disabled={!activeSelection}
                      variant="contained"
                      color="info"
                      onClick={() => handleExport({})}
                      startIcon={
                        <DownloadIcon
                          stroke={
                            activeSelection
                              ? theme.palette.grey[700]
                              : theme.palette.grey[300]
                          }
                          fontSize="small"
                        />
                      }
                    >
                      Download selection
                    </Button>
                    <Button
                      variant="contained"
                      color="primary"
                      startIcon={
                        <AddAntibodyIcon
                          sx={{
                            width: "0.9rem",
                          }}
                        />
                      }
                      href="/add"
                    >
                      Submit an antibody
                    </Button>
                  </Stack>
                </Box>
              </Box>
            </HideOnScroll>
            <TableToolbar
              showFilterMenu={showFilterMenu}
              activeTab={activeTab}
            />
          </Stack>
        </Container>
      </AppBar>
      <Box sx={{ height: "12.5rem" }} component="div" />
    </Box>
  );
};

export default HomeHeader;
