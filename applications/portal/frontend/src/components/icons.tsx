import * as React from "react";
import SvgIcon, { SvgIconProps } from "@mui/material/SvgIcon";

export const HelpIcon = (props: SvgIconProps) => (
  <SvgIcon viewBox="-3 -3 26 26" {...props}>
    <path
      d="M7.57533 7.49984C7.77125 6.94289 8.15795 6.47326 8.66695 6.17411C9.17596 5.87497 9.77441 5.76562 10.3563 5.86543C10.9382 5.96524 11.466 6.26777 11.8462 6.71944C12.2264 7.17111 12.4345 7.74277 12.4337 8.33317C12.4337 9.99984 9.93366 10.8332 9.93366 10.8332M10.0003 14.1665H10.0087M18.3337 9.99984C18.3337 14.6022 14.6027 18.3332 10.0003 18.3332C5.39795 18.3332 1.66699 14.6022 1.66699 9.99984C1.66699 5.39746 5.39795 1.6665 10.0003 1.6665C14.6027 1.6665 18.3337 5.39746 18.3337 9.99984Z"
      stroke="#98A2B3"
      strokeWidth="1.66667"
      strokeLinecap="round"
      strokeLinejoin="round"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
    />
  </SvgIcon>
);

export const SearchIcon = (props: SvgIconProps) => (
  <SvgIcon viewBox="0 0 18 18" {...props}>
    <path
      d="M16.5 16.5L11.5001 11.5M13.1667 7.33333C13.1667 10.555 10.555 13.1667 7.33333 13.1667C4.11167 13.1667 1.5 10.555 1.5 7.33333C1.5 4.11167 4.11167 1.5 7.33333 1.5C10.555 1.5 13.1667 4.11167 13.1667 7.33333Z"
      stroke={props.stroke || "#98A2B3"}
      strokeWidth="1.5"
      strokeLinecap="round"
      strokeLinejoin="round"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
    />
  </SvgIcon>
);

export const SlashIcon = (props: SvgIconProps) => (
  <SvgIcon viewBox="0 0 16 16" {...props}>
    <path
      d="M4.66699 14.6668L11.3337 1.3335"
      stroke="#98A2B3"
      strokeWidth="1.5"
      strokeLinecap="round"
      strokeLinejoin="round"
    />
  </SvgIcon>
);

export const AddAntibodyIcon = (props: SvgIconProps) => (
  <SvgIcon fontSize="small" viewBox="0 0 14 14" {...props}>
    <path
      d="M7.00033 1.1665V12.8332M1.16699 6.99984H12.8337"
      stroke="white"
      strokeWidth="1.5"
      strokeLinecap="round"
      strokeLinejoin="round"
      fill="none"
    />
  </SvgIcon>
);

export const DownloadIcon = (props: SvgIconProps) => (
  <SvgIcon fontSize="small" viewBox="0 0 20 20" {...props}>
    <path
      d="M6.66699 9.99984L10.0003 13.3332M10.0003 13.3332L13.3337 9.99984M10.0003 13.3332V6.6665M18.3337 9.99984C18.3337 14.6022 14.6027 18.3332 10.0003 18.3332C5.39795 18.3332 1.66699 14.6022 1.66699 9.99984C1.66699 5.39746 5.39795 1.6665 10.0003 1.6665C14.6027 1.6665 18.3337 5.39746 18.3337 9.99984Z"
      strokeWidth="1.5"
      strokeLinecap="round"
      strokeLinejoin="round"
      fill="none"
    />
  </SvgIcon>
);

export const HouseIcon = (props: SvgIconProps) => (
  <SvgIcon
    fontSize="small"
    viewBox="0 0 20 20"
    strokeWidth="1.5"
    strokeLinecap="round"
    strokeLinejoin="round"
    {...props}
  >
    <path
      d="M6.66667 14.1668H13.3333M9.18141 2.30345L3.52949 6.69939C3.15168 6.99324 2.96278 7.14017 2.82669 7.32417C2.70614 7.48716 2.61633 7.67077 2.56169 7.866C2.5 8.08639 2.5 8.3257 2.5 8.80433V14.8334C2.5 15.7669 2.5 16.2336 2.68166 16.5901C2.84144 16.9037 3.09641 17.1587 3.41002 17.3185C3.76654 17.5001 4.23325 17.5001 5.16667 17.5001H14.8333C15.7668 17.5001 16.2335 17.5001 16.59 17.3185C16.9036 17.1587 17.1586 16.9037 17.3183 16.5901C17.5 16.2336 17.5 15.7669 17.5 14.8334V8.80433C17.5 8.3257 17.5 8.08639 17.4383 7.866C17.3837 7.67077 17.2939 7.48716 17.1733 7.32417C17.0372 7.14017 16.8483 6.99324 16.4705 6.69939L10.8186 2.30345C10.5258 2.07574 10.3794 1.96189 10.2178 1.91812C10.0752 1.87951 9.92484 1.87951 9.78221 1.91812C9.62057 1.96189 9.47418 2.07574 9.18141 2.30345Z"
      fill="none"
    />
  </SvgIcon>
);

export const SendIcon = (props: SvgIconProps) => (
  <SvgIcon
    fontSize="small"
    viewBox="0 0 18 18"
    strokeWidth="1.5"
    strokeLinecap="round"
    strokeLinejoin="round"
    {...props}
  >
    <path
      d="M7.74928 10.2501L16.4993 1.50014M7.85559 10.5235L10.0457 16.1552C10.2386 16.6513 10.3351 16.8994 10.4741 16.9718C10.5946 17.0346 10.7381 17.0347 10.8587 16.972C10.9978 16.8998 11.0946 16.6518 11.2881 16.1559L16.78 2.08281C16.9547 1.63516 17.0421 1.41133 16.9943 1.26831C16.9528 1.1441 16.8553 1.04663 16.7311 1.00514C16.5881 0.957356 16.3643 1.0447 15.9166 1.21939L1.84349 6.71134C1.34759 6.90486 1.09965 7.00163 1.02739 7.14071C0.964749 7.26129 0.964833 7.40483 1.02761 7.52533C1.10004 7.66433 1.3481 7.7608 1.84422 7.95373L7.47589 10.1438C7.5766 10.183 7.62695 10.2026 7.66935 10.2328C7.70693 10.2596 7.7398 10.2925 7.7666 10.3301C7.79685 10.3725 7.81643 10.4228 7.85559 10.5235Z"
      fill="none"
    />
  </SvgIcon>
);

export const FilteringIcon = (props: SvgIconProps) => (
  <SvgIcon
    width="20"
    height="20"
    viewBox="0 0 20 20"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
    stroke="#667085"
    strokeWidth="1.66667"
    strokeLinecap="round"
    strokeLinejoin="round"
    {...props}
  >
    <path d="M5 10H15M2.5 5H17.5M7.5 15H12.5" />
  </SvgIcon>
);

export const SettingsIcon = (props: SvgIconProps) => (
  <SvgIcon
    width="20"
    height="20"
    viewBox="0 0 20 20"
    xmlns="http://www.w3.org/2000/svg"
    stroke="#667085"
    strokeWidth="1.66667"
    strokeLinecap="round"
    strokeLinejoin="round"
    {...props}
  >
    <path
      d="M2.5 6.6665L12.5 6.6665M12.5 6.6665C12.5 8.04722 13.6193 9.1665 15 9.1665C16.3807 9.1665 17.5 8.04722 17.5 6.6665C17.5 5.28579 16.3807 4.1665 15 4.1665C13.6193 4.1665 12.5 5.28579 12.5 6.6665ZM7.5 13.3332L17.5 13.3332M7.5 13.3332C7.5 14.7139 6.38071 15.8332 5 15.8332C3.61929 15.8332 2.5 14.7139 2.5 13.3332C2.5 11.9525 3.61929 10.8332 5 10.8332C6.38071 10.8332 7.5 11.9525 7.5 13.3332Z"
      fill="none"
    />
  </SvgIcon>
);

export const CheckedIcon = (props: SvgIconProps) => (
  <SvgIcon
    sx={{ height: "1.25rem", width: "1.25rem" }}
    viewBox="0 0 20 20"
    xmlns="http://www.w3.org/2000/svg"
    {...props}
  >
    <rect
      x="0.5"
      y="0.5"
      width="19"
      height="19"
      rx="5.5"
      stroke="#2173F2"
      fill="none"
    />
    <path
      d="M14.6666 6.5L8.24992 12.9167L5.33325 10"
      stroke="#2173F2"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
      fill="none"
    />
  </SvgIcon>
);

export const CheckIcon = (props: SvgIconProps) => (
  <SvgIcon
    viewBox="0 0 20 20"
    xmlns="http://www.w3.org/2000/svg"
    {...props}
  >
    <path
      d="M16.6663 5L7.49967 14.1667L3.33301 10"
      stroke="white"
      strokeWidth="1.66667"
      strokeLinecap="round"
      strokeLinejoin="round"
      fill="none"
    />
  </SvgIcon>
)
export const UncheckedIcon = (props: SvgIconProps) => (
  <SvgIcon
    sx={{ height: "1.25rem", width: "1.25rem" }}
    viewBox="0 0 20 20"
    xmlns="http://www.w3.org/2000/svg"
    {...props}
  >
    <rect
      x="0.5"
      y="0.5"
      width="19px"
      height="19px"
      rx="5.5"
      stroke="#D0D5DD"
      fill="white"
    />
  </SvgIcon>
);

export const FilteredColumnIcon = (props: SvgIconProps) => (
  <SvgIcon
    sx={{ width: "1.1rem", height: "1.1rem" }}
    viewBox="0 0 16 16"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
    {...props}
  >
    <g clipPath="url(#clip0_801_17210)">
      <path
        d="M4 8H12M2 4H14M6 12H10"
        stroke="#667085"
        strokeWidth="1.5"
        strokeLinecap="round"
        strokeLinejoin="round"
      />
      <circle
        cx="13"
        cy="3"
        r="3.75"
        fill="#2173F2"
        stroke="#F9FAFB"
        strokeWidth="1.5"
      />
    </g>
    <defs>
      <clipPath id="clip0_801_17210">
        <rect width="16" height="16" fill="white" />
      </clipPath>
    </defs>
  </SvgIcon>
);

export const SortingIcon = (props: SvgIconProps) => (
  <SvgIcon
    sx={{ height: "0.75rem", width: "0.5rem " }}
    viewBox="0 0 8 12"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
    {...props}
  >
    <path
      d="M0.666748 7.99984L4.00008 11.3332L7.33341 7.99984"
      fill="#98A2B3"
    />
    <path
      d="M0.666748 3.99984L4.00008 0.666504L7.33341 3.99984"
      fill="#98A2B3"
    />
  </SvgIcon>
);

export const AscSortedIcon = (props: SvgIconProps) => (
  <SvgIcon
    sx={{ height: "0.75rem", width: "0.5rem " }}
    viewBox="0 0 8 12"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
    {...props}
  >
    <path
      d="M0.666748 7.99984L4.00008 11.3332L7.33341 7.99984"
      fill="#98A2B3"
    />
    <path
      d="M0.666748 3.99984L4.00008 0.666504L7.33341 3.99984"
      // TODO: change fill color with the right one
      fill="#475467"
    />
  </SvgIcon>
);

export const DescSortedIcon = (props: SvgIconProps) => (
  <SvgIcon
    sx={{ height: "0.75rem", width: "0.5rem " }}
    viewBox="0 0 8 12"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
    {...props}
  >
    <path
      d="M0.666748 7.99984L4.00008 11.3332L7.33341 7.99984"
      // TODO: change fill color with the right one
      fill="#475467"
    />
    <path
      d="M0.666748 3.99984L4.00008 0.666504L7.33341 3.99984"
      fill="#98A2B3"
    />
  </SvgIcon>
);

export const FaqIcon = (props: SvgIconProps) => (
  <SvgIcon viewBox="0 -6 28 24" fill="none" {...props}>
    <path
      d="M13 5.99968L5 5.99967M13 1.99968L5 1.99967M13 9.99968L5 9.99967M2.33333 5.99967C2.33333 6.36786 2.03486 6.66634 1.66667 6.66634C1.29848 6.66634 1 6.36786 1 5.99967C1 5.63148 1.29848 5.33301 1.66667 5.33301C2.03486 5.33301 2.33333 5.63148 2.33333 5.99967ZM2.33333 1.99967C2.33333 2.36786 2.03486 2.66634 1.66667 2.66634C1.29848 2.66634 1 2.36786 1 1.99967C1 1.63148 1.29848 1.33301 1.66667 1.33301C2.03486 1.33301 2.33333 1.63148 2.33333 1.99967ZM2.33333 9.99967C2.33333 10.3679 2.03486 10.6663 1.66667 10.6663C1.29848 10.6663 1 10.3679 1 9.99967C1 9.63148 1.29848 9.33301 1.66667 9.33301C2.03486 9.33301 2.33333 9.63148 2.33333 9.99967Z"
      stroke="#667085"
      strokeWidth="1.5"
      strokeLinecap="round"
      strokeLinejoin="round"
    />
  </SvgIcon>
);

export const EmailIcon = (props: SvgIconProps) => (
  <SvgIcon viewBox="0 -6 28 24" fill="none" {...props}>
    <path
      d="M14.333 11.0003L9.90444 7.00033M6.09491 7.00033L1.66636 11.0003M1.33301 3.66699L6.77629 7.47729C7.21707 7.78583 7.43746 7.94011 7.67718 7.99986C7.88894 8.05265 8.11041 8.05265 8.32217 7.99986C8.56189 7.94011 8.78228 7.78583 9.22306 7.47729L14.6663 3.66699M4.53301 12.3337H11.4663C12.5864 12.3337 13.1465 12.3337 13.5743 12.1157C13.9506 11.9239 14.2566 11.618 14.4484 11.2416C14.6663 10.8138 14.6663 10.2538 14.6663 9.13366V4.86699C14.6663 3.74689 14.6663 3.18683 14.4484 2.75901C14.2566 2.38269 13.9506 2.07673 13.5743 1.88498C13.1465 1.66699 12.5864 1.66699 11.4663 1.66699H4.53301C3.4129 1.66699 2.85285 1.66699 2.42503 1.88498C2.0487 2.07673 1.74274 2.38269 1.55099 2.75901C1.33301 3.18683 1.33301 3.74689 1.33301 4.86699V9.13366C1.33301 10.2538 1.33301 10.8138 1.55099 11.2416C1.74274 11.618 2.0487 11.9239 2.42503 12.1157C2.85285 12.3337 3.4129 12.3337 4.53301 12.3337Z"
      stroke="#667085"
      strokeWidth="1.5"
      strokeLinecap="round"
      strokeLinejoin="round"
      fill="none"
    />
  </SvgIcon>
);

export const InfoIcon = (props: SvgIconProps) => (
  <SvgIcon viewBox="0 -5.5 28 24" fill="none" {...props}>
    <path
      d="M7 9.66667V7M7 4.33333H7.00667M4.2 13H9.8C10.9201 13 11.4802 13 11.908 12.782C12.2843 12.5903 12.5903 12.2843 12.782 11.908C13 11.4802 13 10.9201 13 9.8V4.2C13 3.0799 13 2.51984 12.782 2.09202C12.5903 1.71569 12.2843 1.40973 11.908 1.21799C11.4802 1 10.9201 1 9.8 1H4.2C3.0799 1 2.51984 1 2.09202 1.21799C1.71569 1.40973 1.40973 1.71569 1.21799 2.09202C1 2.51984 1 3.0799 1 4.2V9.8C1 10.9201 1 11.4802 1.21799 11.908C1.40973 12.2843 1.71569 12.5903 2.09202 12.782C2.51984 13 3.0799 13 4.2 13Z"
      stroke="#667085"
      strokeWidth="1.5"
      strokeLinecap="round"
      strokeLinejoin="round"
      fill="none"
    />
  </SvgIcon>
);
export const InfoIconCircle = (props: SvgIconProps) => (
  <SvgIcon viewBox="0 0 20 20" {...props}>
    <path
      d="M10.0003 13.3332V9.99984M10.0003 6.6665H10.0087M18.3337 9.99984C18.3337 14.6022 14.6027 18.3332 10.0003 18.3332C5.39795 18.3332 1.66699 14.6022 1.66699 9.99984C1.66699 5.39746 5.39795 1.6665 10.0003 1.6665C14.6027 1.6665 18.3337 5.39746 18.3337 9.99984Z"
      stroke="#98A2B3"
      strokeWidth="1.5"
      strokeLinecap="round"
      strokeLinejoin="round"
      xmlns="http://www.w3.org/2000/svg"
      fill="none"
    />
  </SvgIcon>
);
export const InfoIconCircleActive = (props: SvgIconProps) => (
  <SvgIcon viewBox="0 0 20 20" {...props}>
    <path
      d="M10.0003 13.3332V9.99984M10.0003 6.6665H10.0087M18.3337 9.99984C18.3337 14.6022 14.6027 18.3332 10.0003 18.3332C5.39795 18.3332 1.66699 14.6022 1.66699 9.99984C1.66699 5.39746 5.39795 1.6665 10.0003 1.6665C14.6027 1.6665 18.3337 5.39746 18.3337 9.99984Z"
      stroke="#2173F2"
      strokeWidth="1.5"
      strokeLinecap="round"
      strokeLinejoin="round"
      xmlns="http://www.w3.org/2000/svg"
      fill="none"
    />
  </SvgIcon>
);

export const FilterIcon = (props: SvgIconProps) => (
  <SvgIcon viewBox="-3 -2.5 21 15" fill="none" fontSize="small" {...props}>
    <path
      d="M3 5H11M1 1H13M5 9H9"
      stroke="#667085"
      strokeWidth="1.5"
      strokeLinecap="round"
      strokeLinejoin="round"
    />
  </SvgIcon>
);

export const SortByIcon = (props: SvgIconProps) => (
  <SvgIcon viewBox="-5 -5 24 24" fill="none" fontSize="small" {...props}>
    <path
      d="M10.3333 1.66699V12.3337M10.3333 12.3337L7.66667 9.66699M10.3333 12.3337L13 9.66699M3.66667 12.3337V1.66699M3.66667 1.66699L1 4.33366M3.66667 1.66699L6.33333 4.33366"
      stroke="#667085"
      strokeWidth="1.5"
      strokeLinecap="round"
      strokeLinejoin="round"
    />
  </SvgIcon>
);

export const ViewLayoutIcon = (props: SvgIconProps) => (
  <SvgIcon viewBox="-5 -5 23 23" fill="none" fontSize="small" {...props}>
    <path
      d="M1 5H13M5 5L5 13M4.2 1H9.8C10.9201 1 11.4802 1 11.908 1.21799C12.2843 1.40973 12.5903 1.71569 12.782 2.09202C13 2.51984 13 3.0799 13 4.2V9.8C13 10.9201 13 11.4802 12.782 11.908C12.5903 12.2843 12.2843 12.5903 11.908 12.782C11.4802 13 10.9201 13 9.8 13H4.2C3.07989 13 2.51984 13 2.09202 12.782C1.71569 12.5903 1.40973 12.2843 1.21799 11.908C1 11.4802 1 10.9201 1 9.8V4.2C1 3.07989 1 2.51984 1.21799 2.09202C1.40973 1.71569 1.71569 1.40973 2.09202 1.21799C2.51984 1 3.0799 1 4.2 1Z"
      stroke="#667085"
      strokeWidth="1.5"
      strokeLinecap="round"
      strokeLinejoin="round"
      fill="none"
    />
  </SvgIcon>
);

export const BackIcon = (props: SvgIconProps) => (
  <SvgIcon viewBox="0 0 17 13" fontSize="small" {...props}>
    <path
      d="M1 4.49996H12.25C14.3211 4.49996 16 6.17889 16 8.24996C16 10.321 14.3211 12 12.25 12H8.5M1 4.49996L4.33333 1.16663M1 4.49996L4.33333 7.83329"
      stroke="#667085"
      strokeWidth="1.66667"
      strokeLinecap="round"
      strokeLinejoin="round"
      fill="none"
    />
  </SvgIcon>
);
export const StepIcon = (props: SvgIconProps) => (
  <SvgIcon viewBox="0 0 17 13" fontSize="small" {...props}>
    <rect width="24" height="24" rx="12" fill="#DFEBF8" />
    <circle cx="12" cy="12" r="4" fill="#2173F2" />
  </SvgIcon>
);

export const CopyIcon = (props: SvgIconProps) => (
  <SvgIcon
    viewBox="0 0 20 20"
    fontSize="small"
    stroke={props.stroke}
    {...props}
  >
    <path
      d="M4.16699 12.5C3.39042 12.5 3.00214 12.5 2.69585 12.3731C2.28747 12.2039 1.96302 11.8795 1.79386 11.4711C1.66699 11.1648 1.66699 10.7765 1.66699 9.99996V4.33329C1.66699 3.39987 1.66699 2.93316 1.84865 2.57664C2.00844 2.26304 2.2634 2.00807 2.57701 1.84828C2.93353 1.66663 3.40024 1.66663 4.33366 1.66663H10.0003C10.7769 1.66663 11.1652 1.66663 11.4715 1.79349C11.8798 1.96265 12.2043 2.28711 12.3735 2.69549C12.5003 3.00177 12.5003 3.39006 12.5003 4.16663M10.167 18.3333H15.667C16.6004 18.3333 17.0671 18.3333 17.4236 18.1516C17.7372 17.9918 17.9922 17.7369 18.152 17.4233C18.3337 17.0668 18.3337 16.6 18.3337 15.6666V10.1666C18.3337 9.23321 18.3337 8.7665 18.152 8.40998C17.9922 8.09637 17.7372 7.8414 17.4236 7.68162C17.0671 7.49996 16.6004 7.49996 15.667 7.49996H10.167C9.23357 7.49996 8.76686 7.49996 8.41034 7.68162C8.09674 7.8414 7.84177 8.09637 7.68198 8.40998C7.50033 8.7665 7.50033 9.23321 7.50033 10.1666V15.6666C7.50033 16.6 7.50033 17.0668 7.68198 17.4233C7.84177 17.7369 8.09674 17.9918 8.41034 18.1516C8.76686 18.3333 9.23357 18.3333 10.167 18.3333Z"
      strokeWidth="1.66667"
      strokeLinecap="round"
      strokeLinejoin="round"
      fill="none"
    />
  </SvgIcon>
);

export const ExternalLinkIcon = (props: SvgIconProps) => (
  <SvgIcon
    viewBox="0 0 20 20"
    fontSize="small"
    stroke={props.stroke}
    {...props}
  >
    <path
      d="M16.5 6.50001L16.5 1.50001M16.5 1.50001H11.5M16.5 1.50001L9 9M7.33333 1.5H5.5C4.09987 1.5 3.3998 1.5 2.86502 1.77248C2.39462 2.01217 2.01217 2.39462 1.77248 2.86502C1.5 3.3998 1.5 4.09987 1.5 5.5V12.5C1.5 13.9001 1.5 14.6002 1.77248 15.135C2.01217 15.6054 2.39462 15.9878 2.86502 16.2275C3.3998 16.5 4.09987 16.5 5.5 16.5H12.5C13.9001 16.5 14.6002 16.5 15.135 16.2275C15.6054 15.9878 15.9878 15.6054 16.2275 15.135C16.5 14.6002 16.5 13.9001 16.5 12.5V10.6667"
      strokeWidth="1.66667"
      strokeLinecap="round"
      strokeLinejoin="round"
      fill="none"
    />
  </SvgIcon>
);
export const FileQuestionIconActive = (props: SvgIconProps) => (
  <SvgIcon viewBox="0 0 20 20" {...props}>
    <path
      d="M16.6663 7.9165V5.6665C16.6663 4.26637 16.6663 3.56631 16.3939 3.03153C16.1542 2.56112 15.7717 2.17867 15.3013 1.93899C14.7665 1.6665 14.0665 1.6665 12.6663 1.6665H7.33301C5.93288 1.6665 5.23281 1.6665 4.69803 1.93899C4.22763 2.17867 3.84517 2.56112 3.60549 3.03153C3.33301 3.56631 3.33301 4.26637 3.33301 5.6665V14.3332C3.33301 15.7333 3.33301 16.4334 3.60549 16.9681C3.84517 17.4386 4.22763 17.821 4.69803 18.0607C5.23281 18.3332 5.93288 18.3332 7.33301 18.3332H11.6663M11.6663 9.1665H6.66634M8.33301 12.4998H6.66634M13.333 5.83317H6.66634M13.7497 12.5017C13.8965 12.0843 14.1863 11.7323 14.5678 11.5082C14.9493 11.284 15.3978 11.202 15.8339 11.2768C16.27 11.3516 16.6655 11.5783 16.9505 11.9168C17.2354 12.2553 17.3914 12.6838 17.3907 13.1262C17.3907 14.3753 15.5171 14.9998 15.5171 14.9998M15.5413 17.4998H15.5496"
      stroke="#2173F2"
      strokeWidth="1.5"
      strokeLinecap="round"
      strokeLinejoin="round"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
    />
  </SvgIcon>
);
export const FileQuestionIcon = (props: SvgIconProps) => (
  <SvgIcon viewBox="0 0 20 20" {...props}>
    <path
      d="M16.6663 7.9165V5.6665C16.6663 4.26637 16.6663 3.56631 16.3939 3.03153C16.1542 2.56112 15.7717 2.17867 15.3013 1.93899C14.7665 1.6665 14.0665 1.6665 12.6663 1.6665H7.33301C5.93288 1.6665 5.23281 1.6665 4.69803 1.93899C4.22763 2.17867 3.84517 2.56112 3.60549 3.03153C3.33301 3.56631 3.33301 4.26637 3.33301 5.6665V14.3332C3.33301 15.7333 3.33301 16.4334 3.60549 16.9681C3.84517 17.4386 4.22763 17.821 4.69803 18.0607C5.23281 18.3332 5.93288 18.3332 7.33301 18.3332H11.6663M11.6663 9.1665H6.66634M8.33301 12.4998H6.66634M13.333 5.83317H6.66634M13.7497 12.5017C13.8965 12.0843 14.1863 11.7323 14.5678 11.5082C14.9493 11.284 15.3978 11.202 15.8339 11.2768C16.27 11.3516 16.6655 11.5783 16.9505 11.9168C17.2354 12.2553 17.3914 12.6838 17.3907 13.1262C17.3907 14.3753 15.5171 14.9998 15.5171 14.9998M15.5413 17.4998H15.5496"
      stroke="#98A2B3"
      strokeWidth="1.5"
      strokeLinecap="round"
      strokeLinejoin="round"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
    />
  </SvgIcon>
);
export const MessageChatSquareIcon = (props: SvgIconProps) => (
  <SvgIcon viewBox="0 0 20 20" {...props}>
    <path
      d="M8.33366 12.4998L5.77095 15.0946C5.41348 15.4565 5.23475 15.6375 5.08112 15.6502C4.94784 15.6613 4.81734 15.6077 4.73029 15.5062C4.62996 15.3892 4.62996 15.1348 4.62996 14.6261V13.3262C4.62996 12.8698 4.25622 12.5396 3.80466 12.4734V12.4734C2.71178 12.3134 1.85347 11.4551 1.69339 10.3622C1.66699 10.182 1.66699 9.96693 1.66699 9.53687V5.6665C1.66699 4.26637 1.66699 3.56631 1.93948 3.03153C2.17916 2.56112 2.56161 2.17867 3.03202 1.93899C3.5668 1.6665 4.26686 1.6665 5.66699 1.6665H11.8337C13.2338 1.6665 13.9339 1.6665 14.4686 1.93899C14.939 2.17867 15.3215 2.56112 15.5612 3.03153C15.8337 3.56631 15.8337 4.26637 15.8337 5.6665V9.1665M15.8337 18.3332L14.02 17.0722C13.765 16.895 13.6376 16.8064 13.4988 16.7435C13.3757 16.6878 13.2462 16.6472 13.1133 16.6227C12.9635 16.5951 12.8083 16.5951 12.4978 16.5951H11.0003C10.0669 16.5951 9.60019 16.5951 9.24368 16.4134C8.93007 16.2536 8.6751 15.9987 8.51532 15.6851C8.33366 15.3285 8.33366 14.8618 8.33366 13.9284V11.8332C8.33366 10.8998 8.33366 10.433 8.51532 10.0765C8.6751 9.76292 8.93007 9.50795 9.24368 9.34816C9.60019 9.1665 10.0669 9.1665 11.0003 9.1665H15.667C16.6004 9.1665 17.0671 9.1665 17.4236 9.34816C17.7372 9.50795 17.9922 9.76292 18.152 10.0765C18.3337 10.433 18.3337 10.8997 18.3337 11.8332V14.0951C18.3337 14.8716 18.3337 15.2599 18.2068 15.5662C18.0376 15.9746 17.7132 16.2991 17.3048 16.4682C16.9985 16.5951 16.6102 16.5951 15.8337 16.5951V18.3332Z"
      stroke="#98A2B3"
      strokeWidth="1.5"
      strokeLinecap="round"
      strokeLinejoin="round"
      xmlns="http://www.w3.org/2000/svg"
      fill="none"
    />
  </SvgIcon>
);
export const MessageChatSquareIconActive = (props: SvgIconProps) => (
  <SvgIcon viewBox="0 0 20 20" {...props}>
    <path
      d="M8.33366 12.4998L5.77095 15.0946C5.41348 15.4565 5.23475 15.6375 5.08112 15.6502C4.94784 15.6613 4.81734 15.6077 4.73029 15.5062C4.62996 15.3892 4.62996 15.1348 4.62996 14.6261V13.3262C4.62996 12.8698 4.25622 12.5396 3.80466 12.4734V12.4734C2.71178 12.3134 1.85347 11.4551 1.69339 10.3622C1.66699 10.182 1.66699 9.96693 1.66699 9.53687V5.6665C1.66699 4.26637 1.66699 3.56631 1.93948 3.03153C2.17916 2.56112 2.56161 2.17867 3.03202 1.93899C3.5668 1.6665 4.26686 1.6665 5.66699 1.6665H11.8337C13.2338 1.6665 13.9339 1.6665 14.4686 1.93899C14.939 2.17867 15.3215 2.56112 15.5612 3.03153C15.8337 3.56631 15.8337 4.26637 15.8337 5.6665V9.1665M15.8337 18.3332L14.02 17.0722C13.765 16.895 13.6376 16.8064 13.4988 16.7435C13.3757 16.6878 13.2462 16.6472 13.1133 16.6227C12.9635 16.5951 12.8083 16.5951 12.4978 16.5951H11.0003C10.0669 16.5951 9.60019 16.5951 9.24368 16.4134C8.93007 16.2536 8.6751 15.9987 8.51532 15.6851C8.33366 15.3285 8.33366 14.8618 8.33366 13.9284V11.8332C8.33366 10.8998 8.33366 10.433 8.51532 10.0765C8.6751 9.76292 8.93007 9.50795 9.24368 9.34816C9.60019 9.1665 10.0669 9.1665 11.0003 9.1665H15.667C16.6004 9.1665 17.0671 9.1665 17.4236 9.34816C17.7372 9.50795 17.9922 9.76292 18.152 10.0765C18.3337 10.433 18.3337 10.8997 18.3337 11.8332V14.0951C18.3337 14.8716 18.3337 15.2599 18.2068 15.5662C18.0376 15.9746 17.7132 16.2991 17.3048 16.4682C16.9985 16.5951 16.6102 16.5951 15.8337 16.5951V18.3332Z"
      stroke="#2173F2"
      strokeWidth="1.5"
      strokeLinecap="round"
      strokeLinejoin="round"
      xmlns="http://www.w3.org/2000/svg"
      fill="none"
    />
  </SvgIcon>
);
export const AccordionPlusIcon = (props: SvgIconProps) => (
  <SvgIcon viewBox="0 0 24 24" {...props}>
    <path
      d="M12 8V16M8 12H16M22 12C22 17.5228 17.5228 22 12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12Z"
      stroke="#98A2B3"
      strokeWidth="1.5"
      strokeLinecap="round"
      strokeLinejoin="round"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
    />
  </SvgIcon>
);
export const AccordionMinusIcon = (props: SvgIconProps) => (
  <SvgIcon viewBox="0 0 24 24" {...props}>
    <path
      d="M 8 12 H 16 M 22 12 C 22 17.5228 17.5228 22 12 22 C 6.47715 22 2 17.5228 2 12 C 2 6.47715 6.47715 2 12 2 C 17.5228 2 22 6.47715 22 12 Z"
      stroke="rgb(152, 162, 179)"
      strokeWidth="1.5"
      strokeLinecap="round"
      strokeLinejoin="round"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
    />
  </SvgIcon>
);

export const ThreeDotsIcon = (props: SvgIconProps) => (
  <SvgIcon viewBox="-3 -3 26 26" {...props}>
    <path
      xmlns="http://www.w3.org/2000/svg"
      d="M12 13C12.5523 13 13 12.5523 13 12C13 11.4477 12.5523 11 12 11C11.4477 11 11 11.4477 11 12C11 12.5523 11.4477 13 12 13Z"
      stroke="#98A2B3"
      strokeWidth="1.5"
      strokeLinecap="round"
      strokeLinejoin="round"
      fill="none"
    />
    <path
      xmlns="http://www.w3.org/2000/svg"
      d="M12 6C12.5523 6 13 5.55228 13 5C13 4.44772 12.5523 4 12 4C11.4477 4 11 4.44772 11 5C11 5.55228 11.4477 6 12 6Z"
      stroke="#98A2B3"
      strokeWidth="1.5"
      strokeLinecap="round"
      strokeLinejoin="round"
      fill="none"
    />
    <path
      xmlns="http://www.w3.org/2000/svg"
      d="M12 20C12.5523 20 13 19.5523 13 19C13 18.4477 12.5523 18 12 18C11.4477 18 11 18.4477 11 19C11 19.5523 11.4477 20 12 20Z"
      stroke="#98A2B3"
      strokeWidth="1.5"
      strokeLinecap="round"
      strokeLinejoin="round"
      fill="none"
    />
  </SvgIcon>
);
export const UserIcon = (props: SvgIconProps) => (
  <SvgIcon viewBox="0 -2 28 24" {...props}>
    <path
      xmlns="http://www.w3.org/2000/svg"
      d="M13.3337 14C13.3337 13.0696 13.3337 12.6044 13.2188 12.2259C12.9603 11.3736 12.2934 10.7067 11.4411 10.4482C11.0626 10.3333 10.5974 10.3333 9.66699 10.3333H6.33366C5.40328 10.3333 4.93809 10.3333 4.55956 10.4482C3.7073 10.7067 3.04035 11.3736 2.78182 12.2259C2.66699 12.6044 2.66699 13.0696 2.66699 14M11.0003 5C11.0003 6.65685 9.65718 8 8.00033 8C6.34347 8 5.00033 6.65685 5.00033 5C5.00033 3.34315 6.34347 2 8.00033 2C9.65718 2 11.0003 3.34315 11.0003 5Z"
      stroke="#667085"
      strokeWidth="1.5"
      strokeLinecap="round"
      strokeLinejoin="round"
      fill="none"
    />
  </SvgIcon>
);

export const CubeIcon = (props: SvgIconProps) => (
  <SvgIcon viewBox="0 -2 28 24" {...props}>
    <path
      xmlns="http://www.w3.org/2000/svg"
      d="M13.6666 4.85221L7.99998 8.00036M7.99998 8.00036L2.33331 4.85221M7.99998 8.00036L8 14.3337M14 10.7061V5.29468C14 5.06625 14 4.95204 13.9663 4.85017C13.9366 4.76005 13.8879 4.67733 13.8236 4.60754C13.7509 4.52865 13.651 4.47318 13.4514 4.36224L8.51802 1.6215C8.32895 1.51646 8.23442 1.46395 8.1343 1.44336C8.0457 1.42513 7.95431 1.42513 7.8657 1.44336C7.76559 1.46395 7.67105 1.51646 7.48198 1.6215L2.54865 4.36225C2.34896 4.47318 2.24912 4.52865 2.17642 4.60754C2.11211 4.67733 2.06343 4.76005 2.03366 4.85017C2 4.95204 2 5.06625 2 5.29468V10.7061C2 10.9345 2 11.0487 2.03366 11.1506C2.06343 11.2407 2.11211 11.3234 2.17642 11.3932C2.24912 11.4721 2.34897 11.5276 2.54865 11.6385L7.48198 14.3793C7.67105 14.4843 7.76559 14.5368 7.8657 14.5574C7.95431 14.5756 8.0457 14.5756 8.1343 14.5574C8.23442 14.5368 8.32895 14.4843 8.51802 14.3793L13.4514 11.6385C13.651 11.5276 13.7509 11.4721 13.8236 11.3932C13.8879 11.3234 13.9366 11.2407 13.9663 11.1506C14 11.0487 14 10.9345 14 10.7061Z"
      stroke="#667085"
      strokeWidth="1.5"
      strokeLinecap="round"
      strokeLinejoin="round"
      fill="none"
    />
  </SvgIcon>
);

export const LogoutIcon = (props: SvgIconProps) => (
  <SvgIcon viewBox="0 -2 28 24"  {...props}>
    <path
      xmlns="http://www.w3.org/2000/svg"
      d="M10.6667 11.3333L14 8M14 8L10.6667 4.66667M14 8H6M6 2H5.2C4.0799 2 3.51984 2 3.09202 2.21799C2.7157 2.40973 2.40973 2.71569 2.21799 3.09202C2 3.51984 2 4.07989 2 5.2V10.8C2 11.9201 2 12.4802 2.21799 12.908C2.40973 13.2843 2.71569 13.5903 3.09202 13.782C3.51984 14 4.0799 14 5.2 14H6"
      stroke="#667085"
      strokeWidth="1.5"
      strokeLinecap="round"
      strokeLinejoin="round"
      fill="none"
    />
  </SvgIcon>
)

export const EyeIcon = (props: SvgIconProps) => (
  <SvgIcon viewBox="0 0 20 20" {...props}>
    <path
      xmlns="http://www.w3.org/2000/svg"
      d="M2.01677 10.5943C1.90328 10.4146 1.84654 10.3248 1.81477 10.1862C1.79091 10.0821 1.79091 9.91791 1.81477 9.81382C1.84654 9.67523 1.90328 9.58538 2.01677 9.40568C2.95461 7.9207 5.74617 4.16666 10.0003 4.16666C14.2545 4.16666 17.0461 7.9207 17.9839 9.40568C18.0974 9.58538 18.1541 9.67523 18.1859 9.81382C18.2098 9.91791 18.2098 10.0821 18.1859 10.1862C18.1541 10.3248 18.0974 10.4146 17.9839 10.5943C17.0461 12.0793 14.2545 15.8333 10.0003 15.8333C5.74617 15.8333 2.95461 12.0793 2.01677 10.5943Z"
      stroke="black"
      strokeWidth="1.5" /> </SvgIcon>
);

export const AlertIcon = (props: SvgIconProps) => (
  <SvgIcon viewBox="0 0 16 16" fontSize="small"  {...props}>
    <path
      xmlns="http://www.w3.org/2000/svg"
      d="M8.00016 5.33325V7.99992M8.00016 10.6666H8.00683M14.6668 7.99992C14.6668 11.6818 11.6821 14.6666 8.00016 14.6666C4.31826 14.6666 1.3335 11.6818 1.3335 7.99992C1.3335 4.31802 4.31826 1.33325 8.00016 1.33325C11.6821 1.33325 14.6668 4.31802 14.6668 7.99992Z"
      stroke="#F04438"
      strokeWidth="1.33333"
      strokeLinecap="round"
      strokeLinejoin="round"
      fill="none"
    />
    <path
      xmlns="http://www.w3.org/2000/svg"
      d="M10.0003 12.5C11.381 12.5 12.5003 11.3807 12.5003 10C12.5003 8.61929 11.381 7.5 10.0003 7.5C8.61962 7.5 7.50034 8.61929 7.50034 10C7.50034 11.3807 8.61962 12.5 10.0003 12.5Z"
      stroke="black"
      strokeWidth="1.5"
      strokeLinecap="round"
      strokeLinejoin="round" 
      fill="none"
    />
  </SvgIcon>
)

export const EyeOffIcon=(props: SvgIconProps) => (
  <SvgIcon viewBox="0 0 22 22" {...props}>
    <path 
      xmlns="http://www.w3.org/2000/svg" 
      d="M10.7429 5.09232C11.1494 5.03223 11.5686 5 12.0004 5C17.1054 5 20.4553 9.50484 21.5807 11.2868C21.7169 11.5025 21.785 11.6103 21.8231 11.7767C21.8518 11.9016 21.8517 12.0987 21.8231 12.2236C21.7849 12.3899 21.7164 12.4985 21.5792 12.7156C21.2793 13.1901 20.8222 13.8571 20.2165 14.5805M6.72432 6.71504C4.56225 8.1817 3.09445 10.2194 2.42111 11.2853C2.28428 11.5019 2.21587 11.6102 2.17774 11.7765C2.1491 11.9014 2.14909 12.0984 2.17771 12.2234C2.21583 12.3897 2.28393 12.4975 2.42013 12.7132C3.54554 14.4952 6.89541 19 12.0004 19C14.0588 19 15.8319 18.2676 17.2888 17.2766M3.00042 3L21.0004 21M9.8791 9.87868C9.3362 10.4216 9.00042 11.1716 9.00042 12C9.00042 13.6569 10.3436 15 12.0004 15C12.8288 15 13.5788 14.6642 14.1217 14.1213"
      stroke="black" 
      strokeWidth="1.5" 
      strokeLinecap="round" />
  </SvgIcon>
);
export const CompanyIcon = (props: SvgIconProps) => (
  <SvgIcon viewBox="0 0 32 32" fontSize="medium"  {...props}>
    <rect width="32" height="32" rx="16" fill="#DFEBF8" />
    <path
      d="M15.333 15.3333H12.133C11.3863 15.3333 11.0129 15.3333 10.7277 15.4787C10.4768 15.6065 10.2728 15.8105 10.145 16.0613C9.99967 16.3466 9.99967 16.7199 9.99967 17.4667V22M21.9997 22V12.1333C21.9997 11.3866 21.9997 11.0132 21.8544 10.728C21.7265 10.4771 21.5225 10.2732 21.2717 10.1453C20.9864 10 20.6131 10 19.8663 10H17.4663C16.7196 10 16.3462 10 16.061 10.1453C15.8101 10.2732 15.6062 10.4771 15.4783 10.728C15.333 11.0132 15.333 11.3866 15.333 12.1333V22M22.6663 22H9.33301M17.6663 12.6667H19.6663M17.6663 15.3333H19.6663M17.6663 18H19.6663"
      stroke="#2173F2"
      strokeWidth="1.33333"
      strokeLinecap="round"
      strokeLinejoin="round"
      fill="none"
    />
  </SvgIcon>
);

export const UserWithBackgroundIcon = (props: SvgIconProps) => (
  <SvgIcon viewBox="0 0 32 32" fontSize="medium"  {...props}>
    <rect width="32" height="32" rx="16" fill="#DFEBF8" />
    <g clipPath="url(#clip0_1376_17941)">
      <path
        d="M11.5439 20.9589C11.9494 20.0034 12.8963 19.3333 13.9997 19.3333H17.9997C19.1031 19.3333 20.0499 20.0034 20.4555 20.9589M18.6663 14.3333C18.6663 15.806 17.4724 16.9999 15.9997 16.9999C14.5269 16.9999 13.333 15.806 13.333 14.3333C13.333 12.8605 14.5269 11.6666 15.9997 11.6666C17.4724 11.6666 18.6663 12.8605 18.6663 14.3333ZM22.6663 15.9999C22.6663 19.6818 19.6816 22.6666 15.9997 22.6666C12.3178 22.6666 9.33301 19.6818 9.33301 15.9999C9.33301 12.318 12.3178 9.33325 15.9997 9.33325C19.6816 9.33325 22.6663 12.318 22.6663 15.9999Z"
        stroke="#2173F2"
        strokeWidth="1.33333"
        strokeLinecap="round"
        strokeLinejoin="round"
        fill="none"
      />
    </g>
    <defs>
      <clipPath id="clip0_1376_17941">
        <rect width="16" height="16" fill="white" transform="translate(8 8)" />
      </clipPath>
    </defs>
  </SvgIcon>
);

export const HorizontalThreeDotsIcon = (props: SvgIconProps) => (
  <SvgIcon viewBox="0 0 32 32" fontSize="medium"  {...props}>
    <rect width="32" height="32" rx="16" fill="#DFEBF8" />
    <path
      d="M16.0003 16.6666C16.3685 16.6666 16.667 16.3681 16.667 15.9999C16.667 15.6317 16.3685 15.3333 16.0003 15.3333C15.6321 15.3333 15.3337 15.6317 15.3337 15.9999C15.3337 16.3681 15.6321 16.6666 16.0003 16.6666Z"
      stroke="#2173F2"
      strokeWidth="1.33333"
      strokeLinecap="round"
      strokeLinejoin="round"
    />
    <path
      d="M20.667 16.6666C21.0352 16.6666 21.3337 16.3681 21.3337 15.9999C21.3337 15.6317 21.0352 15.3333 20.667 15.3333C20.2988 15.3333 20.0003 15.6317 20.0003 15.9999C20.0003 16.3681 20.2988 16.6666 20.667 16.6666Z"
      stroke="#2173F2"
      strokeWidth="1.33333"
      strokeLinecap="round"
      strokeLinejoin="round"
    />
    <path
      d="M11.3337 16.6666C11.7018 16.6666 12.0003 16.3681 12.0003 15.9999C12.0003 15.6317 11.7018 15.3333 11.3337 15.3333C10.9655 15.3333 10.667 15.6317 10.667 15.9999C10.667 16.3681 10.9655 16.6666 11.3337 16.6666Z"
      stroke="#2173F2"
      strokeWidth="1.33333"
      strokeLinecap="round"
      strokeLinejoin="round"
      fill="none"
    />
  </SvgIcon>
);

export const RefreshIcon = (props: SvgIconProps) => (
  <SvgIcon viewBox="0 0 18 16" fontSize="small"  {...props}>
    <path
      d="M6.12246 14.4728C8.12174 15.3598 10.503 15.3116 12.5421 14.1343C15.93 12.1783 17.0908 7.84618 15.1348 4.45828L14.9265 4.09743M2.86571 11.5417C0.909698 8.1538 2.07048 3.8217 5.45839 1.8657C7.49754 0.68839 9.87875 0.640217 11.878 1.52719M1.07812 11.6114L3.35483 12.2215L3.96488 9.94475M14.0358 6.05479L14.6459 3.77808L16.9226 4.38813"
      stroke="#667085"
      strokeWidth="1.66667"
      strokeLinecap="round"
      strokeLinejoin="round"
      fill="none"
    />
  </SvgIcon>
);

export const CircleCheckIcon = (props: SvgIconProps) => (
  <SvgIcon viewBox="0 0 56 56" {...props}>
    <rect x="4" y="4" width="48" height="48" rx="24" fill="#C2DAF3" />
    <path
      d="M23.5 28L26.5 31L32.5 25M38 28C38 33.5228 33.5228 38 28 38C22.4772 38 18 33.5228 18 28C18 22.4772 22.4772 18 28 18C33.5228 18 38 22.4772 38 28Z"
      stroke="#2173F2"
      strokeWidth="1.5"
      strokeLinecap="round"
      strokeLinejoin="round"
      fill="none"
    />
    <rect
      x="4"
      y="4"
      width="48"
      height="48"
      rx="24"
      stroke="#DFEBF8"
      strokeWidth="8"
      fill="none"
    />
  </SvgIcon>
);

export const CircleAlertIcon = (props: SvgIconProps) => (
  <SvgIcon viewBox="0 0 56 56">
    <rect x="4" y="4" width="48" height="48" rx="24" fill="#FEE4E2" />
    <path
      d="M28 24V28M28 32H28.01M38 28C38 33.5228 33.5228 38 28 38C22.4772 38 18 33.5228 18 28C18 22.4772 22.4772 18 28 18C33.5228 18 38 22.4772 38 28Z"
      stroke="#D92D20"
      strokeWidth="1.5"
      strokeLinecap="round"
      strokeLinejoin="round"
      fill="none"
    />
    <rect
      x="4"
      y="4"
      width="48"
      height="48"
      rx="24"
      stroke="#FEF3F2"
      strokeWidth="8"
      fill="none"
    />
  </SvgIcon>
);
