import { Link } from "@mui/material";
import React from "react";
import { useHistory, useLocation } from "react-router-dom";

interface LinkButtonProps {
  label?: string;
  href?: string;
  onClick?: (e: any) => any;
  className?: string;
}

const LinkButton = (props: LinkButtonProps) => {
  return (
    <Link
      component="button"
      underline="none"
      variant="body2"
      href="#"
      sx={(theme) => ({
        fontWeight: 500,
        color: theme.palette.grey[700],
        px: theme.spacing(1.5),
        py: theme.spacing(1),
        "&.selected": {
          bgcolor: theme.palette.grey[100],
          borderRadius: theme.shape.borderRadius,
          color: theme.palette.grey[900],
        },
      })}
      {...props}
    >
      {props.label}
    </Link>
  );
};

const LINKS = [{ label: "Home", href: ["/", "/submissions"] }, { label: "About", href: ["/about"] }, { label: "FAQ", href:  ["/faq"] }];

const NavLinks = () => {
  const history = useHistory();
  const location = useLocation();

  return (
    <>
      {LINKS.map((link) => (
        <LinkButton key={link.label}
          className={link.href.includes(location.pathname) ? "selected" : ""}
          label={link.label}
          onClick={() => history.push(link.href[0])}
        />
      ))} 
          </>
  );
};

export default NavLinks;
