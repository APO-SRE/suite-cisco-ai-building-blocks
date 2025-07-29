from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.route_v1_platform_get import RouteV1PlatformGET
from ...models.route_v1_platform_put import RouteV1PlatformPUT
from ...types import UNSET, Response, Unset


def _get_kwargs(
    spec_destination: str,
    *,
    body: RouteV1PlatformPUT,
    x_nd_rbac: Union[Unset, str] = UNSET,
    x_aci_username: Union[Unset, str] = UNSET,
    x_aci_sessionid: Union[Unset, str] = UNSET,
    x_aci_usertype: Union[Unset, str] = UNSET,
    x_nd_ui_login: Union[Unset, str] = UNSET,
    x_aci_avpair: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_nd_rbac, Unset):
        headers["X-Nd-Rbac"] = x_nd_rbac

    if not isinstance(x_aci_username, Unset):
        headers["X-Aci-Username"] = x_aci_username

    if not isinstance(x_aci_sessionid, Unset):
        headers["X-Aci-Sessionid"] = x_aci_sessionid

    if not isinstance(x_aci_usertype, Unset):
        headers["X-Aci-Usertype"] = x_aci_usertype

    if not isinstance(x_nd_ui_login, Unset):
        headers["X-Nd-UILogin"] = x_nd_ui_login

    if not isinstance(x_aci_avpair, Unset):
        headers["X-Aci-Avpair"] = x_aci_avpair

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/nexus/infra/api/platform/v1/routes/{spec_destination}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json; charset=utf-8"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, RouteV1PlatformGET]]:
    if response.status_code == 200:
        response_200 = RouteV1PlatformGET.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429
    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, RouteV1PlatformGET]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    spec_destination: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: RouteV1PlatformPUT,
    x_nd_rbac: Union[Unset, str] = UNSET,
    x_aci_username: Union[Unset, str] = UNSET,
    x_aci_sessionid: Union[Unset, str] = UNSET,
    x_aci_usertype: Union[Unset, str] = UNSET,
    x_nd_ui_login: Union[Unset, str] = UNSET,
    x_aci_avpair: Union[Unset, str] = UNSET,
) -> Response[Union[Any, RouteV1PlatformGET]]:
    """Modify a route

     Modify a route

    Args:
        spec_destination (str):
        x_nd_rbac (Union[Unset, str]):
        x_aci_username (Union[Unset, str]):
        x_aci_sessionid (Union[Unset, str]):
        x_aci_usertype (Union[Unset, str]):
        x_nd_ui_login (Union[Unset, str]):
        x_aci_avpair (Union[Unset, str]):
        body (RouteV1PlatformPUT): Resource that represents configuration for a network route, to
            be set on all nodes

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, RouteV1PlatformGET]]
    """

    kwargs = _get_kwargs(
        spec_destination=spec_destination,
        body=body,
        x_nd_rbac=x_nd_rbac,
        x_aci_username=x_aci_username,
        x_aci_sessionid=x_aci_sessionid,
        x_aci_usertype=x_aci_usertype,
        x_nd_ui_login=x_nd_ui_login,
        x_aci_avpair=x_aci_avpair,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    spec_destination: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: RouteV1PlatformPUT,
    x_nd_rbac: Union[Unset, str] = UNSET,
    x_aci_username: Union[Unset, str] = UNSET,
    x_aci_sessionid: Union[Unset, str] = UNSET,
    x_aci_usertype: Union[Unset, str] = UNSET,
    x_nd_ui_login: Union[Unset, str] = UNSET,
    x_aci_avpair: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, RouteV1PlatformGET]]:
    """Modify a route

     Modify a route

    Args:
        spec_destination (str):
        x_nd_rbac (Union[Unset, str]):
        x_aci_username (Union[Unset, str]):
        x_aci_sessionid (Union[Unset, str]):
        x_aci_usertype (Union[Unset, str]):
        x_nd_ui_login (Union[Unset, str]):
        x_aci_avpair (Union[Unset, str]):
        body (RouteV1PlatformPUT): Resource that represents configuration for a network route, to
            be set on all nodes

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, RouteV1PlatformGET]
    """

    return sync_detailed(
        spec_destination=spec_destination,
        client=client,
        body=body,
        x_nd_rbac=x_nd_rbac,
        x_aci_username=x_aci_username,
        x_aci_sessionid=x_aci_sessionid,
        x_aci_usertype=x_aci_usertype,
        x_nd_ui_login=x_nd_ui_login,
        x_aci_avpair=x_aci_avpair,
    ).parsed


async def asyncio_detailed(
    spec_destination: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: RouteV1PlatformPUT,
    x_nd_rbac: Union[Unset, str] = UNSET,
    x_aci_username: Union[Unset, str] = UNSET,
    x_aci_sessionid: Union[Unset, str] = UNSET,
    x_aci_usertype: Union[Unset, str] = UNSET,
    x_nd_ui_login: Union[Unset, str] = UNSET,
    x_aci_avpair: Union[Unset, str] = UNSET,
) -> Response[Union[Any, RouteV1PlatformGET]]:
    """Modify a route

     Modify a route

    Args:
        spec_destination (str):
        x_nd_rbac (Union[Unset, str]):
        x_aci_username (Union[Unset, str]):
        x_aci_sessionid (Union[Unset, str]):
        x_aci_usertype (Union[Unset, str]):
        x_nd_ui_login (Union[Unset, str]):
        x_aci_avpair (Union[Unset, str]):
        body (RouteV1PlatformPUT): Resource that represents configuration for a network route, to
            be set on all nodes

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, RouteV1PlatformGET]]
    """

    kwargs = _get_kwargs(
        spec_destination=spec_destination,
        body=body,
        x_nd_rbac=x_nd_rbac,
        x_aci_username=x_aci_username,
        x_aci_sessionid=x_aci_sessionid,
        x_aci_usertype=x_aci_usertype,
        x_nd_ui_login=x_nd_ui_login,
        x_aci_avpair=x_aci_avpair,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    spec_destination: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: RouteV1PlatformPUT,
    x_nd_rbac: Union[Unset, str] = UNSET,
    x_aci_username: Union[Unset, str] = UNSET,
    x_aci_sessionid: Union[Unset, str] = UNSET,
    x_aci_usertype: Union[Unset, str] = UNSET,
    x_nd_ui_login: Union[Unset, str] = UNSET,
    x_aci_avpair: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, RouteV1PlatformGET]]:
    """Modify a route

     Modify a route

    Args:
        spec_destination (str):
        x_nd_rbac (Union[Unset, str]):
        x_aci_username (Union[Unset, str]):
        x_aci_sessionid (Union[Unset, str]):
        x_aci_usertype (Union[Unset, str]):
        x_nd_ui_login (Union[Unset, str]):
        x_aci_avpair (Union[Unset, str]):
        body (RouteV1PlatformPUT): Resource that represents configuration for a network route, to
            be set on all nodes

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, RouteV1PlatformGET]
    """

    return (
        await asyncio_detailed(
            spec_destination=spec_destination,
            client=client,
            body=body,
            x_nd_rbac=x_nd_rbac,
            x_aci_username=x_aci_username,
            x_aci_sessionid=x_aci_sessionid,
            x_aci_usertype=x_aci_usertype,
            x_nd_ui_login=x_nd_ui_login,
            x_aci_avpair=x_aci_avpair,
        )
    ).parsed
