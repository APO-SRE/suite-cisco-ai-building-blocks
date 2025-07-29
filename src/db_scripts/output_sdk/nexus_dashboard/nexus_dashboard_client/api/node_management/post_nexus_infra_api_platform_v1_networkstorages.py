from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.network_storage_v1_platform_get import NetworkStorageV1PlatformGET
from ...models.network_storage_v1_platform_post import NetworkStorageV1PlatformPOST
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: NetworkStorageV1PlatformPOST,
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
        "method": "post",
        "url": "/nexus/infra/api/platform/v1/networkstorages",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json; charset=utf-8"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, NetworkStorageV1PlatformGET]]:
    if response.status_code == 201:
        response_201 = NetworkStorageV1PlatformGET.from_dict(response.json())

        return response_201
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
) -> Response[Union[Any, NetworkStorageV1PlatformGET]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: NetworkStorageV1PlatformPOST,
    x_nd_rbac: Union[Unset, str] = UNSET,
    x_aci_username: Union[Unset, str] = UNSET,
    x_aci_sessionid: Union[Unset, str] = UNSET,
    x_aci_usertype: Union[Unset, str] = UNSET,
    x_nd_ui_login: Union[Unset, str] = UNSET,
    x_aci_avpair: Union[Unset, str] = UNSET,
) -> Response[Union[Any, NetworkStorageV1PlatformGET]]:
    """Create a network storage

     Create a network storage

    Args:
        x_nd_rbac (Union[Unset, str]):
        x_aci_username (Union[Unset, str]):
        x_aci_sessionid (Union[Unset, str]):
        x_aci_usertype (Union[Unset, str]):
        x_nd_ui_login (Union[Unset, str]):
        x_aci_avpair (Union[Unset, str]):
        body (NetworkStorageV1PlatformPOST): Network attached storage config

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, NetworkStorageV1PlatformGET]]
    """

    kwargs = _get_kwargs(
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
    *,
    client: Union[AuthenticatedClient, Client],
    body: NetworkStorageV1PlatformPOST,
    x_nd_rbac: Union[Unset, str] = UNSET,
    x_aci_username: Union[Unset, str] = UNSET,
    x_aci_sessionid: Union[Unset, str] = UNSET,
    x_aci_usertype: Union[Unset, str] = UNSET,
    x_nd_ui_login: Union[Unset, str] = UNSET,
    x_aci_avpair: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, NetworkStorageV1PlatformGET]]:
    """Create a network storage

     Create a network storage

    Args:
        x_nd_rbac (Union[Unset, str]):
        x_aci_username (Union[Unset, str]):
        x_aci_sessionid (Union[Unset, str]):
        x_aci_usertype (Union[Unset, str]):
        x_nd_ui_login (Union[Unset, str]):
        x_aci_avpair (Union[Unset, str]):
        body (NetworkStorageV1PlatformPOST): Network attached storage config

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, NetworkStorageV1PlatformGET]
    """

    return sync_detailed(
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
    *,
    client: Union[AuthenticatedClient, Client],
    body: NetworkStorageV1PlatformPOST,
    x_nd_rbac: Union[Unset, str] = UNSET,
    x_aci_username: Union[Unset, str] = UNSET,
    x_aci_sessionid: Union[Unset, str] = UNSET,
    x_aci_usertype: Union[Unset, str] = UNSET,
    x_nd_ui_login: Union[Unset, str] = UNSET,
    x_aci_avpair: Union[Unset, str] = UNSET,
) -> Response[Union[Any, NetworkStorageV1PlatformGET]]:
    """Create a network storage

     Create a network storage

    Args:
        x_nd_rbac (Union[Unset, str]):
        x_aci_username (Union[Unset, str]):
        x_aci_sessionid (Union[Unset, str]):
        x_aci_usertype (Union[Unset, str]):
        x_nd_ui_login (Union[Unset, str]):
        x_aci_avpair (Union[Unset, str]):
        body (NetworkStorageV1PlatformPOST): Network attached storage config

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, NetworkStorageV1PlatformGET]]
    """

    kwargs = _get_kwargs(
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
    *,
    client: Union[AuthenticatedClient, Client],
    body: NetworkStorageV1PlatformPOST,
    x_nd_rbac: Union[Unset, str] = UNSET,
    x_aci_username: Union[Unset, str] = UNSET,
    x_aci_sessionid: Union[Unset, str] = UNSET,
    x_aci_usertype: Union[Unset, str] = UNSET,
    x_nd_ui_login: Union[Unset, str] = UNSET,
    x_aci_avpair: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, NetworkStorageV1PlatformGET]]:
    """Create a network storage

     Create a network storage

    Args:
        x_nd_rbac (Union[Unset, str]):
        x_aci_username (Union[Unset, str]):
        x_aci_sessionid (Union[Unset, str]):
        x_aci_usertype (Union[Unset, str]):
        x_nd_ui_login (Union[Unset, str]):
        x_aci_avpair (Union[Unset, str]):
        body (NetworkStorageV1PlatformPOST): Network attached storage config

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, NetworkStorageV1PlatformGET]
    """

    return (
        await asyncio_detailed(
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
