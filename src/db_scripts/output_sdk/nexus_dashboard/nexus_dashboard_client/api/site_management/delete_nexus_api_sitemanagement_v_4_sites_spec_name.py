from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    spec_name: str,
    *,
    force_delete: Union[Unset, str] = UNSET,
    auth_cookie: Union[Unset, str] = UNSET,
    cookie: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(auth_cookie, Unset):
        headers["AuthCookie"] = auth_cookie

    if not isinstance(cookie, Unset):
        headers["Cookie"] = cookie

    params: dict[str, Any] = {}

    params["forceDelete"] = force_delete

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/nexus/api/sitemanagement/v4/sites/{spec_name}",
        "params": params,
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
    force_delete: Union[Unset, str] = UNSET,
    auth_cookie: Union[Unset, str] = UNSET,
    cookie: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Delete a site

     Delete a resource of type Site

    Args:
        spec_name (str):
        force_delete (Union[Unset, str]):
        auth_cookie (Union[Unset, str]):
        cookie (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        spec_name=spec_name,
        force_delete=force_delete,
        auth_cookie=auth_cookie,
        cookie=cookie,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    spec_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    force_delete: Union[Unset, str] = UNSET,
    auth_cookie: Union[Unset, str] = UNSET,
    cookie: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Delete a site

     Delete a resource of type Site

    Args:
        spec_name (str):
        force_delete (Union[Unset, str]):
        auth_cookie (Union[Unset, str]):
        cookie (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        spec_name=spec_name,
        force_delete=force_delete,
        auth_cookie=auth_cookie,
        cookie=cookie,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
