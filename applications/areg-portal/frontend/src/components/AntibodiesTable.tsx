import React, { useEffect, useState } from "react";
//MUI
import { DataGrid, GridColDef, GridRenderCellParams } from "@mui/x-data-grid";
import { Typography, Box, Link } from "@mui/material";

//project imports
import { getAntibodies } from "../services/AntibodiesService";

const StyledBadge = (props) => {
  if (props.field === "vendor") {
    return (
      <Box bgcolor="primary.light" px={0.5} py={0.25} borderRadius="0.25rem">
        <Link component="button" underline="none">
          {props.children}
        </Link>
      </Box>
    );
  } else if (props.field === "clonality") {
    return (
      <Box bgcolor="grey.A200" px={1} py={0.25} borderRadius="1rem">
        {props.children}
      </Box>
    );
  } else return <Box>{props.children}</Box>;
};

const RenderNameAndId = (props: GridRenderCellParams<String>) => {
  return (
    <Box>
      <Typography
        variant="body2"
        align="left"
        color="grey.700"
        fontWeight={500}
      >
        {props.row.ab_name}
      </Typography>
      <Typography
        variant="caption"
        align="left"
        component="div"
        color="grey.500"
      >
        {props.row.ab_id}
      </Typography>
    </Box>
  );
};

const RenderCellContent = (props: GridRenderCellParams<String>) => {
  return (
    <StyledBadge {...props}>
      <Typography
        variant="caption"
        align="left"
        color={props.field === "vendor" ? "primary.main" : "grey.500"}
        component="div"
      >
        {props.field === "target_ant_spec"
          ? `${props.row.ab_target} ${props.row.target_species}`
          : props.value}
      </Typography>
    </StyledBadge>
  );
};

const columnsDefaultProps = {
  flex: 1,
  renderCell: RenderCellContent,
  headerClassName: "custom-header",
};

const dataGridStyles = {
  "& .MuiDataGrid-row:hover": {
    backgroundColor: "grey.50",
  },
  "& .MuiDataGrid-columnHeadersInner": {
    backgroundColor: "grey.50",
  },
  "& .MuiDataGrid-columnHeaderTitle": {
    color: "grey.500",
    fontWeight: 600,
    fontSize: "0.875rem",
  },
  " .MuiDataGrid-columnSeparator": {
    display: "none",
  },
  "& .custom-header": {
    borderRight: "0.063rem solid",
    borderColor: "grey.200",
  },
  "& .MuiCheckbox-root svg": {
    width: "1.25rem",
    height: "1.25rem",
    backgroundColor: "common.white",
    border: "0.063rem solid",
    borderColor: "grey.300",
    borderRadius: "0.375rem",
  },
  "& .MuiCheckbox-root svg path": {
    display: "none",
  },
};
const columns: GridColDef[] = [
  {
    ...columnsDefaultProps,
    field: "ab_name",
    headerName: "Name",
    hide: true,
  },
  {
    ...columnsDefaultProps,
    field: "ab_id",
    headerName: "ID",
    hide: true,
  },
  {
    ...columnsDefaultProps,
    field: "ab_name_id",
    headerName: "Name & ID",
    flex: 2,
    renderCell: RenderNameAndId,
    headerAlign: "left",
    align: "left",
  },
  {
    ...columnsDefaultProps,
    field: "ab_target",
    headerName: "Target antigen",
    hide: true,
  },
  {
    ...columnsDefaultProps,
    field: "target_species",
    headerName: "Target species",
    hide: true,
  },
  {
    ...columnsDefaultProps,
    field: "target_ant_spec",
    headerName: "Target antigen",
    flex: 1.5,
  },
  {
    ...columnsDefaultProps,
    field: "proper_citation",
    headerName: "Proper citation",
    flex: 2,
  },
  {
    ...columnsDefaultProps,
    field: "clonality",
    headerName: "Clonality",
  },
  {
    ...columnsDefaultProps,
    field: "reference",
    headerName: "Reference",
    flex: 1.5,
  },
  {
    ...columnsDefaultProps,
    field: "comments",
    headerName: "Comments",
    flex: 3,
    align: "left",
  },
  {
    ...columnsDefaultProps,
    field: "clone_id",
    headerName: "Clone ID",
  },
  {
    ...columnsDefaultProps,
    field: "host",
    headerName: "Host organism",
    flex: 1.5,
  },
  {
    ...columnsDefaultProps,
    field: "vendor",
    headerName: "Link to Vendor",
    flex: 1.5,
  },
  {
    ...columnsDefaultProps,
    field: "catalog_num",
    headerName: "Cat Num",
  },
];

function AntibodiesTable() {
  const [antibodiesList, setAntibodiesList] = useState([]);

  const fetchAntibodies = () => {
    getAntibodies()
      .then((res) => {
        return setAntibodiesList(res);
      })
      .catch((err) => alert(err));
  };

  useEffect(fetchAntibodies, []);

  return (
    <Box sx={{ height: "80vh" }}>
      <Box
        sx={{
          display: "flex",
          height: "100%",
        }}
      >
        <Box sx={{ flexGrow: 1 }}>
          <DataGrid
            sx={dataGridStyles}
            disableColumnMenu
            rows={antibodiesList}
            columns={columns}
            pageSize={20}
            rowsPerPageOptions={[20]}
            checkboxSelection
            disableSelectionOnClick
            getRowHeight={() => "auto"}
          />
        </Box>
      </Box>
    </Box>
  );
}

export default AntibodiesTable;
