from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    spec_name: str,
    *,
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
        "method": "delete",
        "url": f"/nexus/infra/api/platform/v1/networkstorages/{spec_name}",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 202:
        return None
    if response.status_code == 204:
        return None
    if response.status_code == 401:
        return None
    if response.status_code == 403:
        return None
    if response.status_code == 404:
        return None
    if response.status_code == 429:
        return None
    if response.status_code == 500:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    spec_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    x_nd_rbac: Union[Unset, str] = UNSET,
    x_aci_username: Union[Unset, str] = UNSET,
    x_aci_sessionid: Union[Unset, str] = UNSET,
    x_aci_usertype: Union[Unset, str] = UNSET,
    x_nd_ui_login: Union[Unset, str] = UNSET,
    x_aci_avpair: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Delete a network storage

     Delete a network storage

    Args:
        spec_name (str):
        x_nd_rbac (Union[Unset, str]):
        x_aci_username (Union[Unset, str]):
        x_aci_sessionid (Union[Unset, str]):
        x_aci_usertype (Union[Unset, str]):
        x_nd_ui_login (Union[Unset, str]):
        x_aci_avpair (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        spec_name=spec_name,
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


async def asyncio_detailed(
    spec_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    x_nd_rbac: Union[Unset, str] = UNSET,
    x_aci_username: Union[Unset, str] = UNSET,
    x_aci_sessionid: Union[Unset, str] = UNSET,
    x_aci_usertype: Union[Unset, str] = UNSET,
    x_nd_ui_login: Union[Unset, str] = UNSET,
    x_aci_avpair: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Delete a network storage

     Delete a network storage

    Args:
        spec_name (str):
        x_nd_rbac (Union[Unset, str]):
        x_aci_username (Union[Unset, str]):
        x_aci_sessionid (Union[Unset, str]):
        x_aci_usertype (Union[Unset, str]):
        x_nd_ui_login (Union[Unset, str]):
        x_aci_avpair (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        spec_name=spec_name,
        x_nd_rbac=x_nd_rbac,
        x_aci_username=x_aci_username,
        x_aci_sessionid=x_aci_sessionid,
        x_aci_usertype=x_aci_usertype,
        x_nd_ui_login=x_nd_ui_login,
        x_aci_avpair=x_aci_avpair,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
