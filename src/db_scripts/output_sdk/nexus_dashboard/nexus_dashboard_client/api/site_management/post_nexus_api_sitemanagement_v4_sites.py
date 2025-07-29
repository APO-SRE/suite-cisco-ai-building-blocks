from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.site_v4_sitemanagement_get import SiteV4SitemanagementGET
from ...models.site_v4_sitemanagement_post import SiteV4SitemanagementPOST
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: SiteV4SitemanagementPOST,
    force_add: Union[Unset, str] = UNSET,
    auth_cookie: Union[Unset, str] = UNSET,
    cookie: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(auth_cookie, Unset):
        headers["AuthCookie"] = auth_cookie

    if not isinstance(cookie, Unset):
        headers["Cookie"] = cookie

    params: dict[str, Any] = {}

    params["forceAdd"] = force_add

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/nexus/api/sitemanagement/v4/sites",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, SiteV4SitemanagementGET]]:
    if response.status_code == 201:
        response_201 = SiteV4SitemanagementGET.from_dict(response.json())

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
) -> Response[Union[Any, SiteV4SitemanagementGET]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SiteV4SitemanagementPOST,
    force_add: Union[Unset, str] = UNSET,
    auth_cookie: Union[Unset, str] = UNSET,
    cookie: Union[Unset, str] = UNSET,
) -> Response[Union[Any, SiteV4SitemanagementGET]]:
    """Create a site

     Create a resource of type Site

    Args:
        force_add (Union[Unset, str]):
        auth_cookie (Union[Unset, str]):
        cookie (Union[Unset, str]):
        body (SiteV4SitemanagementPOST): Site Resource

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SiteV4SitemanagementGET]]
    """

    kwargs = _get_kwargs(
        body=body,
        force_add=force_add,
        auth_cookie=auth_cookie,
        cookie=cookie,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SiteV4SitemanagementPOST,
    force_add: Union[Unset, str] = UNSET,
    auth_cookie: Union[Unset, str] = UNSET,
    cookie: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, SiteV4SitemanagementGET]]:
    """Create a site

     Create a resource of type Site

    Args:
        force_add (Union[Unset, str]):
        auth_cookie (Union[Unset, str]):
        cookie (Union[Unset, str]):
        body (SiteV4SitemanagementPOST): Site Resource

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SiteV4SitemanagementGET]
    """

    return sync_detailed(
        client=client,
        body=body,
        force_add=force_add,
        auth_cookie=auth_cookie,
        cookie=cookie,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SiteV4SitemanagementPOST,
    force_add: Union[Unset, str] = UNSET,
    auth_cookie: Union[Unset, str] = UNSET,
    cookie: Union[Unset, str] = UNSET,
) -> Response[Union[Any, SiteV4SitemanagementGET]]:
    """Create a site

     Create a resource of type Site

    Args:
        force_add (Union[Unset, str]):
        auth_cookie (Union[Unset, str]):
        cookie (Union[Unset, str]):
        body (SiteV4SitemanagementPOST): Site Resource

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SiteV4SitemanagementGET]]
    """

    kwargs = _get_kwargs(
        body=body,
        force_add=force_add,
        auth_cookie=auth_cookie,
        cookie=cookie,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SiteV4SitemanagementPOST,
    force_add: Union[Unset, str] = UNSET,
    auth_cookie: Union[Unset, str] = UNSET,
    cookie: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, SiteV4SitemanagementGET]]:
    """Create a site

     Create a resource of type Site

    Args:
        force_add (Union[Unset, str]):
        auth_cookie (Union[Unset, str]):
        cookie (Union[Unset, str]):
        body (SiteV4SitemanagementPOST): Site Resource

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SiteV4SitemanagementGET]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            force_add=force_add,
            auth_cookie=auth_cookie,
            cookie=cookie,
        )
    ).parsed
