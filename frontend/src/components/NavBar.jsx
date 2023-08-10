import React from "react";
import { Link } from "react-router-dom";
import { logo } from "../assets";

function NavBar() {
  return (
    <div>
      <nav
        className="flex-no-wrap relative flex w-full items-center justify-between bg-[#11101d] py-2 shadow-md shadow-black/5  lg:flex-wrap lg:justify-start lg:py-4"
        data-te-navbar-ref
      >
        <div className="flex w-full flex-wrap items-center justify-between px-3">
          <Link
            to="/"
            className="block border-0 bg-transparent px-2 text-neutral-500 hover:no-underline hover:shadow-none focus:no-underline focus:shadow-none focus:outline-none focus:ring-0 dark:text-neutral-200 "
          >
            <img src={logo} alt="hoobank" className="w-[124px] h-[32px]" />
          </Link>
          {/* <span className="[&>svg]:w-7">
            </span> */}

          <div
            className="!visible hidden flex-grow basis-[100%] items-center lg:!flex lg:basis-auto"
            id="navbarSupportedContent1"
            data-te-collapse-item
          >
            <ul
              className="list-style-none mr-auto flex flex-col pl-0 lg:flex-row"
              data-te-navbar-nav-ref
            >
              <li className="mb-4 lg:mb-0 lg:pr-2" data-te-nav-item-ref>
                <Link
                  className="text-neutral-500 transition duration-200 hover:text-neutral-700 hover:ease-in-out focus:text-neutral-700 disabled:text-black/30 motion-reduce:transition-none dark:text-neutral-200 dark:hover:text-neutral-300 dark:focus:text-neutral-300 lg:px-2 [&.active]:text-black/90 dark:[&.active]:text-zinc-400"
                  to="/"
                  data-te-nav-link-ref
                >
                  Home
                </Link>
              </li>
              <li className="mb-4 lg:mb-0 lg:pr-2" data-te-nav-item-ref>
                <Link
                  className="text-neutral-500 transition duration-200 hover:text-neutral-700 hover:ease-in-out focus:text-neutral-700 disabled:text-black/30 motion-reduce:transition-none dark:text-neutral-200 dark:hover:text-neutral-300 dark:focus:text-neutral-300 lg:px-2 [&.active]:text-black/90 dark:[&.active]:text-neutral-400"
                  to="#"
                  data-te-nav-link-ref
                >
                  About
                </Link>
              </li>
              <li className="mb-4 lg:mb-0 lg:pr-2" data-te-nav-item-ref>
                <Link
                  className="text-neutral-500 transition duration-200 hover:text-neutral-700 hover:ease-in-out focus:text-neutral-700 disabled:text-black/30 motion-reduce:transition-none dark:text-neutral-200 dark:hover:text-neutral-300 dark:focus:text-neutral-300 lg:px-2 [&.active]:text-black/90 dark:[&.active]:text-neutral-400"
                  to="/list"
                  data-te-nav-link-ref
                >
                  List
                </Link>
              </li>
            </ul>
          </div>

          <div className="relative flex items-center">
            <div className="relative" data-te-dropdown-ref>
              <Link
                className="hidden-arrow flex items-center whitespace-nowrap transition duration-150 ease-in-out motion-reduce:transition-none"
                href="#"
                id="dropdownMenuButton2"
                role="button"
                data-te-dropdown-toggle-ref
                aria-expanded="false"
              >
                <img
                  src="https://tecdn.b-cdn.net/img/new/avatars/2.jpg"
                  className="rounded-full"
                  style={{ height: "25px", width: "25px" }}
                  alt=""
                  loading="lazy"
                />
              </Link>
              <ul
                className="absolute left-auto right-0 z-[1000] float-left m-0 mt-1 hidden min-w-max list-none overflow-hidden rounded-lg border-none bg-white bg-clip-padding text-left text-base shadow-lg dark:bg-neutral-700 [&[data-te-dropdown-show]]:block"
                aria-labelledby="dropdownMenuButton2"
                data-te-dropdown-menu-ref
              >
                <li>
                  <Link
                    className="block w-full whitespace-nowrap bg-transparent px-4 py-2 text-sm font-normal text-neutral-700 hover:bg-neutral-100 active:text-neutral-800 active:no-underline disabled:pointer-events-none disabled:bg-transparent disabled:text-neutral-400 dark:text-neutral-200 dark:hover:bg-white/30"
                    href="#"
                    data-te-dropdown-item-ref
                  >
                    Action
                  </Link>
                </li>
                <li>
                  <Link
                    className="block w-full whitespace-nowrap bg-transparent px-4 py-2 text-sm font-normal text-neutral-700 hover:bg-neutral-100 active:text-neutral-800 active:no-underline disabled:pointer-events-none disabled:bg-transparent disabled:text-neutral-400 dark:text-neutral-200 dark:hover:bg-white/30"
                    href="#"
                    data-te-dropdown-item-ref
                  >
                    Another action
                  </Link>
                </li>
                <li>
                  <Link
                    className="block w-full whitespace-nowrap bg-transparent px-4 py-2 text-sm font-normal text-neutral-700 hover:bg-neutral-100 active:text-neutral-800 active:no-underline disabled:pointer-events-none disabled:bg-transparent disabled:text-neutral-400 dark:text-neutral-200 dark:hover:bg-white/30"
                    href="#"
                    data-te-dropdown-item-ref
                  >
                    Something else here
                  </Link>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </nav>
    </div>
  );
}

export default NavBar;
